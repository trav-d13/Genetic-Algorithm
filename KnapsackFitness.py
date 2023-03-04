## Knapsack key values
weight_penalty = - 10
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


def calculate_knapsack_fitness(genome):
    fitness = 0
    weight = 0
    genes = genome_to_genes_knapsack(genome)  # Determine genes from genome
    for gene in genes:
        gene_value, gene_weight = retrieve_encoding_value(gene)  # Determine the weight and price of the gene encoding
        fitness = fitness + gene_value  # Alter the fitness based on price
        weight = weight + gene_weight  # Increment the weight
    if weight > weight_threshold:  # Weight is too heavy
        fitness = fitness + weight_penalty  # Apply overweight penalty
    return fitness


def retrieve_encoding_value(gene):
    gene_weight = 0
    try:
        gene_value = encodings[gene]['price']  # Get gene price
        gene_weight = encodings[gene]['weight']  # Get gene weight
    except KeyError:  # Gene is not specified/ encoded
        gene_value = invalid_gene_penalty  # Apply invalid gene penalty
    return gene_value, gene_weight


def genome_to_genes_knapsack(genome):
    genes = []
    start_index = 0
    end_index = gene_length

    for i in range(int(len(genome) / gene_length)):  # Break genome into 3-tuples representing genes/ items
        genes.append(genome[start_index: end_index])
        start_index = start_index + gene_length
        end_index = end_index + gene_length
    return genes

