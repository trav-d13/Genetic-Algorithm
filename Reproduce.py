import random
from Individual import Individual
from Population import remove_parents

## Reproduction parameters
reproduce_prob = 0.9


def reproduce(breeding_pool: list):
    determiner = random.uniform(0, 1)  # Value to determine if crossover will occur
    parent_1, parent_2 = select_parents(breeding_pool)  # Select parents from breeding pool
    if determiner < reproduce_prob:
        return crossover_gene(parent_1, parent_2)  # Perform crossover reproduction
    remove_parents(parent_1, parent_2)  # Remove parents from the population
    return parent_1, parent_2


def select_parents(breeding_pool: list):
    parent_1_index = random.randint(0, (len(breeding_pool) - 1))  # Randomly select parent 1 index
    parent_2_index = random.randint(0, (len(breeding_pool) - 1))  # Randomly select parent 2 index

    parent_1 = breeding_pool[parent_1_index]  # Identify parent 1
    parent_2 = breeding_pool[parent_2_index]  # Identify parent 2

    breeding_pool[:] = list(set(breeding_pool) - set([parent_1, parent_2]))  # Remove parents from the breeding pool

    return parent_1, parent_2


def crossover(individual_1: Individual, individual_2: Individual):
    genome_1 = individual_1.access_genome()
    genome_2 = individual_2.access_genome()

    crossover_point = random.randint(0, len(genome_1) - 1)
    child_1_genome = genome_1[0: crossover_point] + genome_2[crossover_point:]  # Create child 1 genome
    child_2_genome = genome_2[0: crossover_point] + genome_1[crossover_point:]  # Create child 2 genome

    assert len(child_1_genome) == len(genome_1)
    assert len(child_2_genome) == len(genome_2)

    child_1 = Individual(genome=child_1_genome, problem=individual_1.access_problem())
    child_2 = Individual(genome=child_2_genome, problem=individual_2.access_problem())

    return child_1, child_2


def crossover_gene(individual_1: Individual, individual_2: Individual):  # Crossover explicitly at gene start/ end locations
    genome_1 = individual_1.access_genome()
    genome_2 = individual_2.access_genome()

    crossover_point = random.randint(1, (len(genome_1)/ individual_1.gene_length) - 1)
    child_1_genome = genome_1[0: crossover_point] + genome_2[crossover_point:]  # Create child 1 genome
    child_2_genome = genome_2[0: crossover_point] + genome_1[crossover_point:]  # Create child 2 genome

    assert len(child_1_genome) == len(genome_1)
    assert len(child_2_genome) == len(genome_2)

    child_1 = Individual(genome=child_1_genome, problem=individual_1.access_problem())
    child_2 = Individual(genome=child_2_genome, problem=individual_2.access_problem())

    return child_1, child_2
