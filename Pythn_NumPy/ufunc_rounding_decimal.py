
# Rounding Decimal

import numpy as np
print("<-- Rounding Decimal -->")
"""
    There are primarily five ways of rounding off decimals in NumPy:
    . trunction
    . fix
    . rounding
    . floor
    . ceil
"""

# Truncation
print("-- Truncation --")
arr = np.trunc([-3.15364, 3.6667])
print(arr)

# fix
print("-- Truncation --")
arr1 = np.fix([-3.15364, 3.6667])
print(arr1)

# rounding
print("-- Rounding --")
arr2 = np.round(3.1666, 2)
print(arr2)

# floor
print("-- floor --")
arr3 = np.floor([-3.1666, 3.6667])
print(arr3)

# ceil
print("-- ceil --")
arr4 = np.ceil([-3.1666, 3.6667])
print(arr4)
