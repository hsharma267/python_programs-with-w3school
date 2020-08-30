
# Summations

import numpy as np
print("<-- Summations -->")

# Example
print("-- Example --")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.add(arr1, arr2)
print(newarr)

# Another Example
print("-- Another Example --")
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([5, 6, 7, 8])
newarr1 = np.sum([arr3, arr4])
print(newarr1)

# Summation Over an Axis
print("-- Summation Over an Axis --")
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([5, 6, 7, 8])
newarr2 = np.sum([arr3, arr4], axis=1)
print(newarr2)

# Cummulative Sum
print("-- Cummulative Sum --")
arr5 = np.array([1, 2, 3, 4])
newarr3 = np.cumsum(arr5)
print(newarr3)
