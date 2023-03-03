from Individual import generate_individual
population_size = 1000
def generate_population():
    population = []
    for i in range(population_size):
        population.append(generate_individual())
    return population