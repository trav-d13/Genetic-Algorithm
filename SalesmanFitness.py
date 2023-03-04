import random
import numpy as np

## Salesman Key values
cities = 8
max_distance = 100
gene_length = 3
distances = np.random.randint(low=1, high=max_distance, size=(cities, cities))

self_connecting_penalty = 50
city_repetition_penalty = 50
city_exclusion_penalty = 50
non_closing_penalty = 50

encodings = {
    '000': 0,
    '001': 1,
    '010': 2,
    '011': 3,
    '100': 4,
    '101': 5,
    '110': 6,
    '111': 7
}


def calculate_salesman_fitness(genome):
    fitness = 0
    genes = genome_to_genes_salesman(genome)

    for ind in range(len(genes)):
        connection_ind = retrieve_connection(genes[ind])  # Retrieve the city it is connected to
        if ind == connection_ind:  # City is connected to itself
            fitness = fitness + self_connecting_penalty  # Apply self-loopp penalty
        else:
            fitness = fitness + get_distance(ind, connection_ind)  # Add connection distance
    fitness = fitness + determine_city_repetitions_penalty(genes)  # Multiple connections to the same city (penalty)
    fitness = fitness + determine_city_exclusion_penalty(genes)  # City is excluded from path (penalty)
    return calculate_max_possible_trip() - fitness  # Inverse the fitness value to enable maximization in reproduction (same as knapsack problem)


def calculate_max_possible_trip():
    return cities * max_distance  # Calculate max distance possible


def determine_city_repetitions_penalty(genes: list):
    penalty = 0
    for gene in genes:
        gene_count = genes.count(gene)  # Repetitions of a gene (city connection)
        if gene_count > 1:
            penalty = penalty + gene_count * city_repetition_penalty  # Number of repetitions are proportional to penalty
    return penalty


def determine_city_exclusion_penalty(genes: list):
    penalty = 0
    gene_list = list(encodings.keys())
    for gene in gene_list:
        if genes.count(gene) == 0:  # Gene/ city has been excluded from path
            penalty = penalty + city_exclusion_penalty
    return penalty


def retrieve_connection(gene):
    return encodings[gene]


def get_distance(gene_index: int, mapping):
    return distances[gene_index, mapping]


def genome_to_genes_salesman(genome):
    genes = []
    start_index = 0
    end_index = gene_length

    for i in range(int(len(genome) / gene_length)):  # Break genome into 3-tuples representing genes/ connecting to which cities
        genes.append(genome[start_index: end_index])
        start_index = start_index + gene_length
        end_index = end_index + gene_length
    return genes

