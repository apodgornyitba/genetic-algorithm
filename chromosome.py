# Class color with attributes red, green, blue and methods to convert to and from RGB and CMYK
from fitness import calculate_fitness
from utils.converters import proportion_to_rgb

class Chromosome:
    def __init__(self, palette_proportions):
        self.gens = palette_proportions
        self.fitness = calculate_fitness(self.gens)
        self.color = proportion_to_rgb(self.gens)

    def get_gens(self):
        return self.gens
    
    def get_fitness(self):
        return self.fitness

    def set_gens(self, new_gens):
        self.gens = new_gens

    def __str__(self) -> str:
        return str(self.gens)

    # def set_rgb(self, red, green, blue):
    #     self.rgb = [red, green, blue]

    # def __str__(self):
    #     return "({}, {}, {})".format(self.red, self.green, self.blue)
