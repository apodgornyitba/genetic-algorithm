import random
import numpy as np

from utils.config import Config
from utils.converters import proportion_to_rgb
from chromosome import Chromosome
from fitness import calculate_fitness

# La funcion de mutacion en este caso es aleatoria, 
# se se elige un valor aleatorio para una posición aleatoria del cromosoma. 
# Por ejemplo, podrías cambiar el valor de un componente RGB por un valor aleatorio entre 0 y 255.

Config.load_from_json("config.json")

mutation_probability = Config.mutation["probability"]
palette_color_amount = Config.get_palette_color_amount()

mutation_methods = {
    "limited": (lambda individual: limited_multiple_gene_mutation(individual)),
    "complete": (lambda individual: complete_mutation(individual))
}


def limited_multiple_gene_mutation(individual: Chromosome):
    mutate_amount = Config.mutation['amount']
    if random.uniform(0, 1) <= mutation_probability:
        gens_pos = random.sample(range(palette_color_amount), k=mutate_amount)
        max_val = 0

        for i in gens_pos:
            max_val += individual.gens[i]
        
        for j in gens_pos:
            if j == gens_pos[mutate_amount - 1]:
                individual.gens[j] = max_val
                break
            individual.gens[j] = np.random.uniform(0, max_val)
            max_val -= individual.gens[j]

        # Must recalculate fitness and color on mutation
        individual.fitness = calculate_fitness(individual.gens)
        individual.color = proportion_to_rgb(individual.gens)
    return individual


def complete_mutation(individual: Chromosome):
    if random.uniform(0, 1) <= mutation_probability:
        max_val = 1
        for i in np.arange(Config.get_palette_color_amount()):
            if i == Config.get_palette_color_amount() - 1:
                individual.gens[i] = max_val
                break
            individual.gens[i] = random.uniform(0, max_val)
            max_val -= individual.gens[i]

        # Must recalculate fitness and color on mutation
        individual.fitness = calculate_fitness(individual.gens)
        individual.color = proportion_to_rgb(individual.gens)
    return individual