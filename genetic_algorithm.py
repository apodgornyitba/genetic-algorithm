from math import log
import random
import numpy as np

import sys
import os
import csv

from utils.config import Config
from utils.generate import generate_initial_population
from utils.converters import proportion_to_rgb
from fitness import calculate_fitness

from selection import select_methods
from cross import cross_methods
from mutation import mutation_methods

Config.load_from_json('config.json')

acceptable_solution_value = 0.99

new_gen_selects = {
    "use_all": (lambda old_population, children: fill_all(old_population, children)),
    "new_over_actual": (lambda old_population, children: fill_new_over_actual(old_population, children))
}

class GeneticAlgorithm:
    def run(self, run_number):
        (directory, filename) = create_output_file()
        generations_data = []
        generation = 0
        converged_gens = 0
        population = generate_initial_population(Config.max_population_size)

        while Config.max_generations is not None and generation < Config.max_generations:
            cross_seed = random.uniform(0, 1)
            children = []
            if cross_seed <= Config.cross_over['probability']:
                parents = select_methods[Config.selections['parents']['name']](population, Config.selections['parents']['amount'])

                parent_amount = len(parents)
                parent_pairs = random.sample(range(0, parent_amount), k=parent_amount)
                for i in np.arange(0, parent_amount, 2):
                    new_children = cross_methods[Config.cross_over['name']](parents[parent_pairs[i]], parents[parent_pairs[i+1]])
                    children.extend(new_children)
        
            new_population = population + children
            for individual in new_population:
                mutation_seed = random.uniform(0, 1)
                if mutation_seed <= Config.mutation['probability']:
                    individual = mutation_methods[Config.mutation['name']](individual)
            
            new_population = new_gen_selects[Config.implementation](population, children)
            population = new_population

            min_fitness = population[0].fitness
            max_fitness = population[0].fitness
            max_fitness_individual = population[0]
            avg_fitness = 0.0

            indiv_proportions = {}

            for indiv in population:
                if indiv.color not in indiv_proportions:
                    indiv_proportions[indiv.color] = 0
                indiv_proportions[indiv.color] += 1 / Config.max_population_size
                if indiv.fitness < min_fitness:
                    min_fitness = indiv.fitness
                if indiv.fitness > max_fitness:
                    max_fitness = indiv.fitness
                    max_fitness_individual = indiv
                avg_fitness += indiv.fitness
            
            avg_fitness /= Config.max_population_size
            diversity = shannon_diversity(indiv_proportions)

            generations_data.append({
                'generation': generation,
                'min_fitness': min_fitness,
                'avg_fitness': avg_fitness,
                'max_fitness': max_fitness,
                'diversity': diversity
            })

            if generation > 0 and has_converged([generations_data[generation]['max_fitness'], generations_data[generation-1]['max_fitness']], 1e-2) and has_converged([generations_data[generation]['avg_fitness'], generations_data[generation-1]['avg_fitness']], 1e-1):
                converged_gens += 1
                if converged_gens == 2:
                    break
            else:
                converged_gens = 0
            
            if is_acceptable_solution(max_fitness_individual):
                break
            
            generation += 1

        file_path = os.path.join(directory, filename)
        write_headers = False

        file_option = 'a'
        if run_number == 0:
            file_option = 'w'

        with open(file_path, file_option, encoding='UTF-8', newline='') as file:
            csvwriter = csv.writer(file)
            if file_option == 'w':
                csvwriter.writerow(['run', 'generation', 'min_fitness', 'avg_fitness', 'max_fitness', 'diversity'])
            csvwriter.writerow([run_number] + list(generations_data[-1].values()))
            # for gen_data in generations_data:
            #     csvwriter.writerow([run_number] + list(gen_data.values()))
        
        return max(population, key=lambda chromosome: chromosome.fitness)


def has_converged(numbers, tolerance=1e-3):
    converged = False
    if (len(numbers) < 2):
        return converged
    if (abs(numbers[-1] - numbers[-2]) < tolerance):
        converged = True

    return converged


def is_acceptable_solution(individual):
    individual_color = proportion_to_rgb(individual.get_gens())
    
    return color_similarity(individual_color, Config.color_objective) >= acceptable_solution_value


def color_similarity(rgb1, rgb2):
    """
    Computes the similarity between two colors represented in RGB.
    The similarity is based on the Euclidean distance between the color
    in the RGB color space.
    
    Args:
    rgb1: A tuple of three integers representing the first color in RGB.
    rgb2: A tuple of three integers representing the second color in RGB.
    
    Returns:
    A float between 0 and 1 representing the similarity between the colors.
    A value of 1 indicates that the colors are identical, while a value of 0
    indicates that the colors are completely different.
    """
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    distance = ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5
    max_distance = ((255 ** 2) * 3) ** 0.5  # Maximum possible distance
    similarity = 1 - distance / max_distance
    return similarity


def shannon_diversity(indiv_proportions):
    diversity = 0
    for indiv in indiv_proportions:
        diversity -= indiv_proportions[indiv] * log(indiv_proportions[indiv])
    return diversity


def create_output_file():
    argc = len(sys.argv)
    sub_directory = ''
    if argc == 2:
        sub_directory = sys.argv[1]
    
    # Options are:
    # 'i': implementations
    # 'c': crosses
    # 'm': mutations
    # 's': selections
    # default: other

    root_directory = 'results'
    directory = root_directory
    filename = ''

    if not os.path.exists('results'):
        os.makedirs('results')

    match sub_directory:
        case 'i':
            directory += '/implementations'
            if not os.path.exists(directory):
                os.makedirs(directory)
            filename = '{}_{}.csv'.format(Config.implementation, Config.selections['new_gen']['amount'])
        case 'c':
            directory += '/crosses'
            if not os.path.exists(directory):
                os.makedirs(directory)
            filename = '{}-{}.csv'.format(Config.cross_over['name'], Config.cross_over['probability'])
        case 'm':
            directory += '/mutations'
            if not os.path.exists(directory):
                os.makedirs(directory)
            filename = '{}-{}.csv'.format(Config.mutation['name'], Config.mutation['probability'])
        case 's':
            directory += '/selections'
            if not os.path.exists(directory):
                os.makedirs(directory)
            filename = '{}-{}_{}-{}.csv'.format(Config.selections['parents']['name'], Config.selections['parents']['amount'], Config.selections['new_gen']['name'], Config.selections['parents']['amount'])
        case _:
            directory += '/other'
            if not os.path.exists(directory):
                os.makedirs(directory)
            filename = 'other.csv'.format()
    
    return (directory, filename)


def fill_all(old_population, children):
    population = old_population + children
    return select_methods[Config.selections['new_gen']['name']](population, Config.max_population_size)

    
def fill_new_over_actual(old_population, children):
    if not children:
        return fill_all(old_population, children)
    new_population = select_methods[Config.selections['new_gen']['name']](children, Config.selections['new_gen']['amount'])
    new_population_amount = len(new_population)
    if new_population_amount < Config.max_population_size:
        new_population = new_population + select_methods[Config.selections['new_gen']['name']](old_population, Config.max_population_size - new_population_amount)
    return new_population

