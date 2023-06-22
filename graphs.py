import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('./results/implementations/use_all.csv')

def one_run():
    # Extract the rows with run number 0
    df_run0 = df[df['run'] == 0]

    # Extract the required data
    generation = df_run0['generation']
    min_fitness = df_run0['min_fitness']
    avg_fitness = df_run0['avg_fitness']
    max_fitness = df_run0['max_fitness']
    diversity = df_run0['diversity']

    # Create the plot
    plt.plot(generation, min_fitness, label='Min Fitness')
    plt.plot(generation, avg_fitness, label='Avg Fitness')
    plt.plot(generation, max_fitness, label='Max Fitness')
    # plt.plot(generation, diversity, label='Diversity')
    plt.xlabel('Generation')
    plt.ylabel('Fitness and Diversity')
    plt.title('Fitness and Diversity over Generations (Run 0)')
    plt.legend()
    plt.show()

one_run()
