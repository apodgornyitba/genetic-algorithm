import numpy as np
import random
from chromosome import Chromosome
from utils.config import Config

def generate_random_palette(size: int):
    return [ (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)) for _ in range(size)]

def generate_initial_population(population_size: int):
    population = []
    for _ in np.arange(population_size):
        genes = []
        for i in np.arange(Config.get_palette_color_amount()):
            max_val = 1
            for j in np.arange(i):
                max_val -= genes[j]
            gene_value = random.uniform(0, max_val)
            if i == Config.get_palette_color_amount() - 1:
                gene_value = max_val
            genes.append(gene_value)
        population.append(Chromosome(genes))
    return population
    
    # return [ Chromosome(np.random.rand(Config.get_palette_color_amount())) for _ in range(population_size) ]