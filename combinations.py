from itertools import combinations, permutations, combinations_with_replacement

print(list(combinations([1,2,3], 2))) # All possible permutations for [1,2,3] -> (1, 2, 3), (1, 3, 2) ...
print(list(combinations('abc', 2))) 
print(list(combinations_with_replacement('abc', 2))) # Repeated values allowed
print(list(permutations('abc', 2))) 