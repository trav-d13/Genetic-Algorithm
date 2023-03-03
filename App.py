from Population import generate_population
from Selection import select_breeding_pool
from Reproduce import reproduce
from Mutate import mutate

# Knapsack Problem = 0
# Travelling Salesman problem = 1

## Genetic Algorithm Parameters ##
generations = 1
population = 20
breeding_pool_size = 10

if __name__ == "__main__":
    population = generate_population()

    generation = 0
    while generation < generations:
        breeding_pool = select_breeding_pool(population=population,
                                             breeding_pool_size=breeding_pool_size)  # Generate breeding pool

        child_1, child_2 = reproduce(breeding_pool)  # Reproduction (probability of reproduction inside method)
        child_1, child_2 = mutate(child_1, child_2)  # Mutate (probability of reproduction inside method)

        print("Generation: ", generation)
        generation += 1
