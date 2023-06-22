import numpy as np

select_methods = {
    "elite": (lambda population, num_selected: select_elite(population, num_selected)),
    "roulette": (lambda population, num_selected: select_roulette(population, num_selected)),
    "universal": (lambda population, num_selected: select_universal(population, num_selected)),
    "deterministic_tournament": (lambda population, num_selected: select_deterministic_tournament(population, num_selected))
}

def select_elite(population, num_selected):
    sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
    return sorted_population[0:num_selected]

def select_roulette(population, num_selected):
    fitness_scores = [chromosome.fitness for chromosome in population]
    fitness_sum = sum(fitness_scores)
    probabilities = [fitness / fitness_sum for fitness in fitness_scores]
    cumulative_probabilities = np.cumsum(probabilities)
    selected_indices = []
    for i in range (num_selected):
        point = np.random.uniform(0, 1)
        index = np.searchsorted(cumulative_probabilities, point)
        selected_indices.append(index)       
    return [population[i] for i in selected_indices]

def select_universal(population, num_selected):
    fitness_scores = [chromosome.fitness for chromosome in population]
    fitness_sum = sum(fitness_scores)
    probabilities = [fitness / fitness_sum for fitness in fitness_scores]
    cumulative_probabilities = np.cumsum(probabilities)
    selected_indices = []
    for i in range(num_selected):
        start_point = np.random.uniform(0, 1)
        point = (start_point + i) / num_selected
        index = np.searchsorted(cumulative_probabilities, point)
        selected_indices.append(index)
    return [population[i] for i in selected_indices]

# TODO: tournament_size = M, la cantidad de individuos a elegir de los N disponibles en la poblacion. La pregunta es, que valor tiene M?
def select_deterministic_tournament(population, num_selected):
    tournament_size = 100
    selected = []
    pop_len = len(population)

    i = 0
    while i < num_selected:
        tournament_indices = np.random.randint(0, pop_len, tournament_size)
        
        max_fitness_idx = tournament_indices[0]
        max_fitness = population[max_fitness_idx].fitness

        for j in tournament_indices:
           if population[j].fitness > max_fitness:
               max_fitness = population[j].fitness
               max_fitness_idx = j
        
        selected.append(population[j])
        i += 1
    return selected
