import random
from KnapsackFitness import calculate_knapsack_fitness
from KnapsackFitness import genome_to_genes_knapsack
from SalesmanFitness import calculate_salesman_fitness
from SalesmanFitness import genome_to_genes_salesman


class Individual:
    def __init__(self, genome=None, problem=0):
        ## Knapsack ##
        self.knapsack_length = 15

        ## Travelling Salesman ##
        self.cities = 8
        self.gene_length = 3
        self.salesman_length = self.cities * self.gene_length

        if genome is None:  # Genome creation
            self.genome = self.generate_genome(problem)  # Randomly generate
        else:
            self.genome = genome  # Utilize genome param

        self.problem = problem  # Individual created to solve what problem
        self.fitness = self.calculate_fitness(self.genome, self.problem)  # Fitness

    def generate_genome(self, problem):
        genome_length = self.knapsack_length
        if problem == 1:
            genome_length = self.salesman_length
        genome_str = ''.join(random.choices(['0', '1'], k=genome_length))  # Generate random binary genome
        assert len(genome_str) == genome_length
        return genome_str

    def calculate_fitness(self, genome, problem):
        if problem == 0:
            return calculate_knapsack_fitness(genome)
        else:
            return calculate_salesman_fitness(genome)

    def access_genome(self):
        return self.genome

    def access_fitness(self):
        return self.fitness

    def access_problem(self):
        return self.problem

    def display_genome(self):
        if self.problem == 0:
            return genome_to_genes_knapsack(self.genome)
        else:
            return genome_to_genes_salesman(self.genome)
