import random
from KnapsackFitness import calculate_fitness


class Individual:
    def __init__(self, genome=None):
        ## Knapsack ##
        self.knapsack_length = 15

        ## Travelling Salesman ##
        self.cities = 5
        self.gene_length = 5
        self.salesman_length = self.cities * self.gene_length

        if genome is None:  # Genome creation
            self.genome = self.generate_genome()  # Randomly generate
        else:
            self.genome = genome  # Utilize genome param

        self.fitness, self.weight = calculate_fitness(self.genome)  # Fitness

    def generate_genome(self):
        genome_str = ''.join(random.choices(['0', '1'], k=self.knapsack_length))  # Generate random binary genome
        assert len(genome_str) == self.knapsack_length
        return genome_str

    def access_genome(self):
        return self.genome

    def access_fitness(self):
        return self.fitness
