from Population import generate_population, add_children, avg_population_fitness_bounded,  find_fittest_individual_bounded
from Selection import select_breeding_pool
from Reproduce import reproduce
from Mutate import mutate


## Genetic Algorithm Parameters ##
# Utilize README to determine problem specific parameters
generations = 1000
population = 20
breeding_pool_size = 10

## Problem Selection ##
# 0 - Knapsack Problem
# 1 - Travelling Salesman
knapsack = 0
travelling_salesman = 1

if __name__ == "__main__":
    population = generate_population(pop_size=population, problem=travelling_salesman)

    generation = 0
    while generation < generations:
        breeding_pool = select_breeding_pool(population=population,
                                             breeding_pool_size=breeding_pool_size)  # Generate breeding pool
        while len(breeding_pool) > 0:
            child_1, child_2 = reproduce(breeding_pool)  # Reproduction (probability of reproduction inside method, and parent removal)
            child_1, child_2 = mutate(child_1, child_2)  # Mutate (probability of reproduction inside method)
            add_children(child_1, child_2)  # Add children into the population

        fittest_individual = find_fittest_individual_bounded()  # Identify the population's fittest individual
        avg_fitness = avg_population_fitness_bounded()  # Calculate the avg population fitness

        print('#############################################################')  # Use README to decode results
        print("Generation: ", generation, ' | Generation avg fitness: ', avg_fitness, " | Max fitness: ",
              fittest_individual.access_fitness(), " | Genome: ", fittest_individual.display_genome())
        generation += 1  # Increment generation
