from Individual import Individual


def generate_population(size=1000):
    population = []
    for i in range(size):
        population.append(Individual())
    return population