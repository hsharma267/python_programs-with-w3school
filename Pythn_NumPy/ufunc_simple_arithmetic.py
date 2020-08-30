

# Simple Aritmatic

import numpy as np
print("<-- Simple Arithmatic -->")

# Addition
print("-- Addition --")
arr1 = np.array([10, 12, 45, 75])
arr2 = np.array([56, 85, 52, 75])
newarr = np.add(arr1, arr2)
print(newarr)

# Subtraction
print("-- Subtraction --")
arr3 = np.array([10, 12, 45, 75])
arr4 = np.array([56, 85, 52, 75])
newarr1 = np.subtract(arr4, arr3)
print(newarr1)

# Multiplication
print("-- Multiplication --")
arr5 = np.array([10, 12, 45, 75])
arr6 = np.array([56, 85, 52, 75])
newarr2 = np.multiply(arr5, arr6)
print(newarr2)

# Division
print("-- Division --")
arr7 = np.array([10, 12, 45, 75])
arr8 = np.array([56, 85, 52, 75])
newarr3 = np.divide(arr7, arr8)
print(newarr3)

# power
print("-- Division --")
arr9 = np.array([10, 12, 45, 60])
arr10 = np.array([4, 5, 2, 3])
newarr4 = np.power(arr9, arr10)
print(newarr4)

# Remainder
print("-- Remainder --")
arr11 = np.array([10, 20, 30, 40])
arr12 = np.array([3, 7, 9, 8])
newarr5 = np.mod(arr11, arr12)
print(newarr5)

print("-- Another example --")
arr13 = np.array([10, 20, 30, 40])
arr14 = np.array([3, 7, 9, 8])
newarr6 = np.remainder(arr13, arr14)
print(newarr6)

# Quotient and mod
print("-- Quotient and mod --")
arr15 = np.array([10, 20, 30, 40])
arr16 = np.array([3, 7, 9, 8])
newarr6 = np.divmod(arr15, arr16)
print(newarr6)

# Absolute values
print("-- Absolute values --")
arr17 = np.array([10, -20, 30, -40])
newarr7 = np.absolute(arr17)
print(newarr7)
