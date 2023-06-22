import numpy as np
from utils.config import Config

def calculate_fitness(individual_gens):
    
    target_color = Config.color_objective
    palette = Config.palette

    # Initialize the RGB values for the new color
    new_red = 0
    new_green = 0
    new_blue = 0

    # Loop through each color in the palette and calculate its contribution to the new color
    for i in range(len(palette)):
        new_red += individual_gens[i] * palette[i][0]
        new_green += individual_gens[i] * palette[i][1]
        new_blue += individual_gens[i] * palette[i][2]

    # Truncate the RGB values and create a tuple of the new RGB values
    new_color = [int(new_red), int(new_green), int(new_blue)]

    # Calculate Euclidean distance between the solution color and the desired color
    distance = np.linalg.norm(np.array(target_color) - np.array(new_color))
    # Return inverse distance as fitness score
    return (1 / (1 + distance)) * 1000
    
