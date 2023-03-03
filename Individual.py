import random

## Knapsack ##
knapsack_length = 15

## Travelling Salesman ##
cities = 5
gene_length = 5
salesman_length = cities * gene_length

def generate_individual():
    rand_number = random.getrandbits(knapsack_length)
    genome_str = format(rand_number, '0b')
    return genome_str
