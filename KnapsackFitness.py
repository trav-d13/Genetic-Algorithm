weight_penalty = 10
gene_length = 3

encodings = {
    '001': {'weight': 12, 'price': 4},
    '010': {'weight': 1, 'price': 2},
    '011': {'weight': 2, 'price': 2},
    '100': {'weight': 1, 'price': 1},
    '101': {'weight': 4, 'price': 10}
}

def calculate_fitness(genome):
    fitness = 0
    genes = genome_to_genes(genome)
    for gene in genes:
        print(genes[gene].price)



def genome_to_genes(genome):
    genes = []
    start_index = 0
    end_index = gene_length

    for i in range(int(len(genome) / gene_length)):
        genes.append(genome[start_index: end_index])
        start_index + gene_length
        end_index + gene_length

    return genes


if __name__ == "__main__":
    fitness = calculate_fitness('10001101010100')
    print(fitness)