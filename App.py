from Population import generate_population

# Knapsack Problem = 0
# Travelling Salesman problem = 1

## Genetic Algorithm Parameters ##
generations = 5
population = 10

if __name__ == "__main__":
    population = generate_population()
    print(population[0].access_genome())
    print(population[0].access_fitness())

    generation = 0
    while generation < generations:
        print("Generation: ", generation)
        generation += 1
