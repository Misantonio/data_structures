# Combinations and Permutations
from itertools import product, permutations

# Product
print(list(product([1,2,3], [1,3,5]))) # All possible combinations -> (1,1), (1,3), (1,5) ...
print(list(product([1,2], repeat=3)))
print("")

# Permutations
print(list(permutations([1,2,3]))) # All possible permutations for [1,2,3] -> (1, 2, 3), (1, 3, 2) ...
print(list(permutations('abc', 3))) 

