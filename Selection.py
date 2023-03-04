import random

## Tournament selection param ##
winner_selection_prob = 0.6
runner_up_prob = winner_selection_prob + 0.25


# Adapt method selection method to utilize roulette or tournament
def select_breeding_pool(population, breeding_pool_size, tournament_size=5):
    breeding_pool = []
    for i in range(breeding_pool_size):
        selected_individual = roulette_selection(population)
        breeding_pool.append(selected_individual)
    return breeding_pool


## Roulette Selection ##
def roulette_selection(population):
    wheel = roulette_wheel(population)  # Create roulette wheel
    selector = random.uniform(0, 1)  # Generate a selector for the wheel
    individual = population[0]
    for wheel_value in wheel:  # Determine selected Individual
        if wheel_value < selector:
            individual = wheel[wheel_value]
        else:
            break

    return individual


def roulette_wheel(population):
    current_prob = 0
    bounded_total_fitness = fitness_total_bounded(population)  # Roulette wheel must not have negative fitness
    roulette = dict()

    for individual in population:
        fitness = individual.access_fitness()  # Individual's fitness
        if fitness < 0:
            fitness = 0  # Eliminate negative fitness values
        probability = fitness / bounded_total_fitness  # Probability of selection
        current_prob = current_prob + probability  # Update roulette wheel probability
        roulette[current_prob] = individual  # Assign roulette wheel ranges to individual
    return roulette


def fitness_total_bounded(population) -> float:  # Eliminate negative fitness values
    fitness_sum = 0
    for individual in population:
        fitness = individual.access_fitness()
        if fitness < 0: fitness = 0
        fitness_sum = fitness_sum + fitness
    return fitness_sum


## Tournament Selection ##

def tournament(population, tournament_size):
    pool = create_tournament_pool(population, tournament_size)  # Select population pool
    sorted_pool = select_tournament_winners(pool)  # Sort the pool's fitness
    selection_prob = random.uniform(0, 1)
    if selection_prob < winner_selection_prob:
        return sorted_pool[0]
    elif selection_prob < runner_up_prob:
        return sorted_pool[1]
    else:
        return sorted_pool[2]


def create_tournament_pool(population, tournament_size):
    tournament_pool = []
    for i in range(tournament_size):
        individual_index = random.randint(0, len(population) - 1)  # Randomly generate index in population
        tournament_pool.append(population[individual_index])
    return tournament_pool


def select_tournament_winners(tournament_population):
    sorted_population = sorted(tournament_population, key=lambda x: x.fitness, reverse=True)
    return sorted_population



## Accessory Methods ##
def fitness_total(population) -> float:  # Allow negative fitness values
    fitness_sum = 0
    for individual in population:
        fitness_sum = fitness_sum + individual.access_fitness()
    return fitness_sum
