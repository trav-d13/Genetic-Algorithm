import random
from KnapsackFitness import calculate_fitness


class Individual:
    def __init__(self):
        ## Knapsack ##
        self.knapsack_length = 15

        ## Travelling Salesman ##
        self.cities = 5
        self.gene_length = 5
        self.salesman_length = self.cities * self.gene_length

        ## Individual chromosome
        self.genome = self.generate_genome()
        self.fitness = calculate_fitness(self.genome)

    def generate_genome(self):
        rand_number = random.getrandbits(self.knapsack_length)
        genome_str = format(rand_number, '0b')
        return genome_str

    def access_genome(self):
        return self.genome

    def access_fitness(self):
        return self.fitness
