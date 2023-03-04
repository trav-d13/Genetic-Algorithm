# Genetic-Algorithm
Genetic Algorithm to solve the Knapsack and Travelling Salesman problems. 

**Knapsack Problem:**  \
_Given a set of items, each with a weight and a value, determine which items to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible._ ([Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem)) \
Specifically, each item can be selected multiple times to be put in the Knapsack. 
The problem weights and values are given as follows: 

| weight (Kg) | value ($) |
|-------------|-----------|
| 12          | 4         |
| 1           | 2         |
| 2           | 2         |
| 1           | 1         |
| 4           | 10        |


## Implementation
The Genetic Algorithm Implementation makes use of a binary encoding of the genotypes for both the 
Knapsack Problem and the Travelling Salesman problem. 

### Knapsack
#### Encoding
The genome is encoded as a binary string. \
Each three letter sub-string encodes for a item, resulting in a string of 15 characters fixed length. \
**Note:** Correct the correct problem formulation would include a longer fixed length.

#### Optimal Parameters
Generations: 1000 \
Population: 500 \
Breeding Pool Size: 30

### Travelling Salesman
