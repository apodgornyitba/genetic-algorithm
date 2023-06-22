# fitness vs crossover probability

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

crosses_file_format = './results/crosses/{M}-{P}.csv'


# fitness vs crossover probability
def fitness_vs_probability():
    probability('./results/crosses/uniform-')
    

# fitness vs mutation probability
def fitness_vs_mutation_probability():
    probability('./results/mutations/complete-')


def probabilities_of_different_mutations():
    # mutation file names
    mutation_file_names = ['complete', 'limited']

    # Create empty lists to store data for all probabilities
    probabilities = []
    max_fitnesses_one_gene = []
    max_fitnesses_limited = []
    max_fitnesses_uniform = []
    max_fitnesses_complete = []

    sem_max_fitnesses_one_gene = []
    sem_max_fitnesses_limited = []
    sem_max_fitnesses_uniform = []
    sem_max_fitnesses_complete = []

    for i in range(0, 11):
        probability = i/10
        probabilities.append(probability)
        if i == 0:
            probability = i
        if i == 10:
            probability = 1

        for filename in mutation_file_names:
            filename = './results/mutations/{}-{}.csv'.format(filename, probability)
            df = pd.read_csv(filename)
            
            # Get the min max and average fitness for all run and last generation and its standard error
            if filename == './results/mutations/complete-{}.csv'.format(probability):
                max_fitnesses_complete.append(df["max_fitness"].mean())
                sem_max_fitnesses_complete.append(df["max_fitness"].sem())
            elif filename == './results/mutations/limited-{}.csv'.format(probability):
                max_fitnesses_limited.append(df["max_fitness"].mean())
                sem_max_fitnesses_limited.append(df["max_fitness"].sem())
        

    # Plot data for all probabilities
    plt.errorbar(probabilities, max_fitnesses_complete, yerr=sem_max_fitnesses_complete, label="Maximo Fitness (Mutacion Completa)")
    plt.errorbar(probabilities, max_fitnesses_limited, yerr=sem_max_fitnesses_limited, label="Maximo Fitness (Mutacion Limitada)")

    plt.legend()
    plt.xlabel("Probabilidad de Mutacion")
    plt.title("Fitness vs. Probabilidad de Mutacion")
        
    plt.ylabel("Fitness")
    plt.show()
        

def probability(plot_name):
    # Create empty lists to store data for all probabilities
    probabilities = []
    min_fitnesses = []
    avg_fitnesses = []
    max_fitnesses = []
    sem_min_fitnesses = []
    sem_avg_fitnesses = []
    sem_max_fitnesses = []

    for i in range(0, 11):
        probability = i/10
        probabilities.append(probability)
        if i == 0:
            probability = i
        if i == 10:
            probability = 1
        filename = '{}{}.csv'.format(plot_name, probability)
        df = pd.read_csv(filename)

        # Create a new dataframe selecting the run and his last generation
        grouped = df.groupby('run').last()
        
        # Get the min max and average fitness for all run and last generation and its standard error
        # min_fitnesses.append(grouped["min_fitness"].mean())
        # avg_fitnesses.append(grouped["avg_fitness"].mean())
        max_fitnesses.append(grouped["max_fitness"].mean())
        # sem_min_fitnesses.append(grouped["min_fitness"].sem())
        # sem_avg_fitnesses.append(grouped["avg_fitness"].sem())
        sem_max_fitnesses.append(grouped["max_fitness"].sem())

    # Plot data for all probabilities
    # plt.errorbar(probabilities, min_fitnesses, yerr=sem_min_fitnesses, label="Minimum Fitness")
    # plt.errorbar(probabilities, avg_fitnesses, yerr=sem_avg_fitnesses, label="Average Fitness")
    plt.errorbar(probabilities, max_fitnesses, yerr=sem_max_fitnesses, label="Maximum Fitness")

    plt.legend()
    if plot_name == './results/crosses/uniform-':
        plt.xlabel("Crossover Probability")
        plt.title("Fitness vs. Crossover Probability")
    else:
        plt.xlabel("Mutation Probability")
        plt.title("Fitness vs. Mutation Probability")
        
    plt.ylabel("Fitness")
    plt.show()


def crosses_probabilities():
    crosses = ['one_point', 'uniform']
    colors = ['tab:red', 'tab:blue']
    j = 0

    for cross in crosses:
        # Create empty lists to store data for all probabilities
        probabilities = []

        max_fitnesses = []
        sem_max_fitnesses = []
        for i in range(0, 11):
            probability = i/10
            probabilities.append(probability)
            if i == 0:
                probability = i
            if i == 10:
                probability = 1

            filename = crosses_file_format.replace('{M}', cross).replace('{P}', str(probability))

            # filename = '{}{}.csv'.format(plot_name, probability)
            df = pd.read_csv(filename)

            # Create a new dataframe selecting the run and his last generation
            grouped = df.groupby('run').last()
            
            # Get the min max and average fitness for all run and last generation and its standard error
            max_fitnesses.append(grouped["max_fitness"].mean())
            sem_max_fitnesses.append(grouped["max_fitness"].sem())
            
        plt.errorbar(probabilities, max_fitnesses, yerr=sem_max_fitnesses, marker='o', linestyle='dotted', capsize=4, label=cross, color=colors[j])
        plt.legend()
        j += 1

    plt.xlabel("Probabilidad de cruza")     
    plt.ylabel("Fitness máximo")
    plt.show()

if __name__ == '__main__':
    probabilities_of_different_mutations()
