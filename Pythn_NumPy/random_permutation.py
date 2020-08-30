# Random Permutations

import numpy as np
from numpy import random as rdm
print("<-- Random Permutations -->")

# Shuffling Arrays
arr = np.array([0, 1, 2, 3, 4, 5])
rdm.shuffle(arr)
print(arr)
# Generating Permutations of Arrays
print("-- Generating Permutations of Arrays --")
arr1 = np.array([0, 1, 2, 3, 4, 5])
print(rdm.permutation(arr1))
