# Fitness vs method used
import pandas as pd
import matplotlib.pyplot as plt
import math

# stochastic_files = [
#     './results/selections/elite-250_elite-250.csv',
#     './results/selections/roulette-250_roulette-250.csv',
#     './results/selections/universal-250_universal-250.csv',
#     './results/selections/deterministic_tournament-250_deterministic_tournament-250.csv'
# ]

stochastic_file_format = './results/selections/{M}-{K}_{M}-{K}.csv'
implementation_file_format = './results/implementations/{M}_{K}.csv'

def fitness_by_selection_method():
    fig, ax = plt.subplots(figsize=(12, 8))

    methods = ['elite', 'roulette', 'universal', 'deterministic_tournament']
    bars_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
    K = '500'

    fitnesses = []
    err_fitnesses = []

    for method in methods:
        file = stochastic_file_format.replace('{M}', method)
        file = file.replace('{K}', K)

        df = pd.read_csv(file)
        fitness_col = df['max_fitness']

        fitnesses.append(fitness_col.mean())
        err_fitnesses.append(fitness_col.std())
    
    bars = ax.bar(methods, fitnesses, yerr=err_fitnesses, label=methods, color=bars_colors)
    ax.bar_label(bars, padding=3)
    
    ax.set_ylabel('Fitness máximo')
    ax.set_xlabel('Métodos de selección')
    # ax.set_title('Fitness máximo promedio para cada método')

    plt.show()

def fitness_by_implementation_method():
    fig, ax = plt.subplots(figsize=(12, 8))

    methods = ['use_all', 'new_over_actual']
    bars_colors = ['tab:red', 'tab:blue']
    K = ['500', '1000', '2000', '3000', '4000', '4500']

    fitnesses = []
    err_fitnesses = []

    for method in methods:
        fitnesses = []
        err_fitnesses = []
        for k in K:
            file = implementation_file_format.replace('{M}', method)
            file = file.replace('{K}', k)

            df = pd.read_csv(file)
            fitness_col = df['max_fitness']

            fitnesses.append(fitness_col.mean())
            err_fitnesses.append(fitness_col.std())

        plt.errorbar(K, fitnesses, yerr=err_fitnesses, marker='o', linestyle='dotted', capsize=4, label=method)
        plt.legend()
    
    ax.set_ylabel('Fitness máximo')
    ax.set_xlabel('Cantidad de hijos por generación')
    # bars = ax.bar(methods, fitnesses, yerr=err_fitnesses, label=methods, color=bars_colors)
    # ax.bar_label(bars, padding=3)
    
    # ax.set_ylabel('Fitness')
    # ax.set_title('Fitness promedio para cada método')

    plt.show()

fitness_by_selection_method()
# fitness_by_implementation_method()

#df1 = pd.read_csv('./results/selections/use_all.csv')
#df1 = pd.read_csv('./results/selections/use_all.csv')
#df1 = pd.read_csv('./results/selections/use_all.csv')
#df1 = pd.read_csv('./results/selections/use_all.csv')
