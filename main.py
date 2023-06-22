import numpy as np

from fitness import calculate_fitness
from selection import select_elite, select_roulette
from utils.generate import generate_initial_population
from cross import crossover_one_point
from genetic_algorithm import GeneticAlgorithm, color_similarity
from utils.config import Config

Config.load_from_json('config.json')


def euclidean(a, b):
    return np.linalg.norm(a - b)

def diversity(population):
    unique_chromosomes = set(tuple(chromosome) for chromosome in population)
    return len(unique_chromosomes) / len(population)

# max_generations = Config.break_condition[0]['qty']
# generic_algorithm = GeneticAlgorithm(Config.max_population_size, Config.select_amount_per_generation, max_generations, Config.mutation['probability'])
genetic_algorithm = GeneticAlgorithm()
for i in np.arange(Config.runs):
    best_chromosome = genetic_algorithm.run(i)

    # Initialize the RGB values for the new color
    new_red = 0
    new_green = 0
    new_blue = 0
    # Loop through each color in the palette and calculate its contribution to the new color
    for i in range(Config.get_palette_color_amount()):
        new_red += best_chromosome.gens[i] * Config.palette[i][0]
        new_green += best_chromosome.gens[i] * Config.palette[i][1]
        new_blue += best_chromosome.gens[i] * Config.palette[i][2]

    # Truncate the RGB values and create a tuple of the new RGB values
    new_color = [int(new_red), int(new_green), int(new_blue)]

    print('Palette proportions: {}'.format(['{}%'.format(round(gene * 100, 3)) for gene in best_chromosome.gens]))
    print('Color similarity: {}%'.format(round(color_similarity(new_color, Config.color_objective) * 100, 3)))
    print('Obtained color: {}'.format(new_color))
