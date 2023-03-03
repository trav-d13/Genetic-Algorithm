from Individual import Individual
import random

## Mutation Param
mutation_prob = 0.1  # Low mutation probability
bit_flip_mutation_prob = 0.8
genome_flip_mutation_prob = 0.2


def mutate(individual_1, individual_2):
    return mutate_individual(individual_1), mutate_individual(individual_2)


def mutate_individual(individual: Individual):
    genome = individual.access_genome()  # Access individual's genome
    decider = random.uniform(0, 1)  # Determine if mutation will occur based on decider value

    if decider < mutation_prob:
        mutation_type_decider = random.uniform(0, 1)  # Decider for mutation type
        if mutation_type_decider < bit_flip_mutation_prob:
            return bit_flip_mutation(genome)
        return genome_flip_mutation(genome)


def bit_flip_mutation(genome: str):
    bit_index = random.randint(0, len(genome) - 1)
    bit = int(genome[bit_index])
    flipped_bit = bit ^ 1

    return genome[0: bit_index] + str(flipped_bit) + genome[bit_index + 1:]


def genome_flip_mutation(genome: str):
    encoded_genome = genome.replace('1', '5')  # Alter values of 1's to 5's
    temp_genome = encoded_genome.replace('0', '1')  # Invert 0's to 1's
    return temp_genome.replace('5', '0')  # Replace 5's to o's (1's to 0's inversion)
