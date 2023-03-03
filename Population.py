from Individual import Individual

population = []

def generate_population(size=1000):
    for i in range(size):
        population.append(Individual())
    return population


def remove_parents(parent_1, parent_2):
    for individual in population:
        if individual == parent_1:
            population.remove(individual)
            print('Removed')
        elif individual == parent_2:
            population.remove(individual)
            print('Removed')