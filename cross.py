import random
import copy
from fitness import calculate_fitness
import numpy as np

from chromosome import Chromosome
from utils.config import Config
from utils.converters import proportion_to_rgb

Config.load_from_json("config.json")

palette_color_amount = Config.get_palette_color_amount()

cross_methods = {
    "one_point": (lambda parent1, parent2: crossover_one_point(parent1, parent2)),
    "uniform": (lambda parent1, parent2: crossover_uniform(parent1, parent2))
}

def crossover_one_point(parent1: Chromosome, parent2: Chromosome):
    point = random.randint(0, palette_color_amount - 1)

    child1_gens = copy.deepcopy(parent1.gens)
    child2_gens = copy.deepcopy(parent2.gens)

    for i in range(point, palette_color_amount):
        child1_gens[i] = parent2.gens[i]
        child2_gens[i] = parent1.gens[i]

        sum1 = 0
        sum2 = 0

        for j in np.arange(Config.get_palette_color_amount()):
            sum1 += child1_gens[j]
            sum2 += child2_gens[j]

        child1_gens = [prop/sum1 for prop in child1_gens]
        child2_gens = [prop/sum2 for prop in child2_gens]
    
    child1 = Chromosome(child1_gens)
    child2 = Chromosome(child2_gens)

    return child1, child2

def crossover_uniform(parent1: Chromosome, parent2: Chromosome):
    child1_gens = copy.deepcopy(parent1.gens)
    child2_gens = copy.deepcopy(parent2.gens)

    # TODO: Buscar si se puede usar deepcopy de hijo a padre para evitar tener que copiar valores
    for i in range(palette_color_amount):
        if random.uniform(0, 1) > 0.5:
            child1_gens[i] = parent2.gens[i]
            child2_gens[i] = parent1.gens[i]

            sum1 = 0
            sum2 = 0

            for j in np.arange(Config.get_palette_color_amount()):
                sum1 += child1_gens[j]
                sum2 += child2_gens[j]

            child1_gens = [prop/sum1 for prop in child1_gens]
            child2_gens = [prop/sum2 for prop in child2_gens]
    
    child1 = Chromosome(child1_gens)
    child2 = Chromosome(child2_gens)

    return child1, child2