from Population import generate_population, add_children, avg_population_fitness_bounded,  find_fittest_individual_bounded
from Selection import select_breeding_pool
from Reproduce import reproduce
from Mutate import mutate

# Knapsack Problem = 0
# Travelling Salesman problem = 1

## Genetic Algorithm Parameters ##
generations = 200
population = 100
breeding_pool_size = 30

if __name__ == "__main__":
    population = generate_population()

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

        print('#############################################################')
        print("Generation: ", generation, ' | Generation avg fitness: ', avg_fitness, " | Max fitness: ",
              fittest_individual.access_fitness(), " | Genome: ", fittest_individual.access_genome())
        generation += 1  # Increment generation
