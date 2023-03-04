from Individual import Individual

population = []
size = 0


def generate_population(pop_size=1000, problem: int=0):
    global size
    size = pop_size

    for i in range(size):
        population.append(Individual(problem=problem))
    return population


def remove_parents(parent_1, parent_2):
    for individual in population:
        if individual == parent_1:
            population.remove(individual)
        elif individual == parent_2:
            population.remove(individual)


def add_children(child_1, child_2):
    if len(population) == size - 2:  # Two distinct parents were removed
        population.append(child_1)  # Add child 1 to population
        population.append(child_2)  # Add child 2 to population
    else:  # The same individual was chosen as parent_1 and parent_2 (Very unlikely)
        population.append(child_1)


def find_fittest_individual_bounded() -> Individual:
    max_fitness = -1000
    fittest_individual = population[0]  # Ensure an individual is always returned
    for individual in population:
        fitness = individual.access_fitness()
        if fitness > max_fitness:
            fittest_individual = individual
    return fittest_individual


def avg_population_fitness_bounded():
    global size
    size = len(population)
    fitness_total = 0
    for individual in population:
        fitness = individual.access_fitness()
        fitness_total = fitness_total + fitness
    return fitness_total / size

