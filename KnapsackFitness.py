## Knapsack key values
weight_penalty = - 5
invalid_gene_penalty = - 2
gene_length = 3
weight_threshold = 15

encodings = {
    '001': {'weight': 12, 'price': 4},
    '010': {'weight': 1, 'price': 2},
    '011': {'weight': 2, 'price': 2},
    '100': {'weight': 1, 'price': 1},
    '101': {'weight': 4, 'price': 10}
}


def calculate_fitness(genome):
    fitness = 0
    weight = 0
    genes = genome_to_genes(genome)
    for gene in genes:
        gene_value, gene_weight = retrieve_encoding_value(gene)
        fitness = fitness + gene_value
        weight = weight + gene_weight
    if weight > weight_threshold:
        fitness = fitness + weight_penalty
    return fitness, weight


def retrieve_encoding_value(gene):
    gene_value = 0
    gene_weight = 0
    try:
        gene_value = encodings[gene]['price']
        gene_weight = encodings[gene]['weight']
    except KeyError:
        gene_value = invalid_gene_penalty
    return gene_value, gene_weight


def genome_to_genes(genome):
    genes = []
    start_index = 0
    end_index = gene_length

    for i in range(int(len(genome) / gene_length)):
        genes.append(genome[start_index: end_index])
        start_index = start_index + gene_length
        end_index = end_index + gene_length
    return genes


if __name__ == "__main__":
    fitness = calculate_fitness('101001011101000')
    print(fitness)