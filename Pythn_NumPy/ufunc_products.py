
# Products

import numpy as np
print("<-- Products -->")

# Example
print("-- Example --")
arr = np.array([1, 2, 3, 4])
newarr = np.prod(arr)
print(newarr)

# Another Example
print("-- Another Example --")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 4])
newarr1 = np.prod([arr1, arr2])
print(newarr1)

# Summation Over an Axis
print("-- Summation Over an Axis --")
arr3 = np.array([1, 2, 3, 4])
newarr2 = np.prod([arr3], axis=1)
print(newarr2)

# Cummulative Products
print("-- Cummulative Products")
arr4 = np.array([1, 2, 3, 4])
newarr3 = np.cumprod(arr4)
print(newarr3)
