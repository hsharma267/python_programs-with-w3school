# Create a Numpy ndarray Object

import numpy as np
print("<-- Create a numpy -->")
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Dimension in Arrays
print("<-- Dimension in Arrays -->")

# 0-D Array
print("-- O-D Array --")
arr = np.array(42)
print(arr)

# 1-D Array
print("-- 1-D Array --")
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D Array
print("-- 2-D Array --")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3-D Array
print("-- 3-D Array --")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)

# Create Number of Dimension

print("<-- check no. of dimension -->")
a = np.array(26)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print()
print("Zero dimensional array:", a.ndim)
print("One dimensional array:", b.ndim)
print("Two dimensional array:", c.ndim)
print("Three dimensional array:", d.ndim)

# Higher Dimensional Arrays

print("<-- Higher Dimensionl Arrays -->")
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("Number of Dimension:", arr.ndim)
