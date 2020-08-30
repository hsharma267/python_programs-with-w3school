# Numpy Searching Arrays
import numpy as np
print("<-- NumPy Searching Arrays -->")
arr = np.array([1, 2, 3, 4, 5, 6, 4, 8, 9, 4, 2, 4])
newarr = np.where(arr == 4)
print(newarr)

# Another Example
print("-- Another Example --")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a = np.where(arr1 % 2 == 0)
print(a)

# Another Example1
print("-- Another Example --")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.where(arr1 % 2 == 1)
print(b)

# Search Sorted
print("-- Search Sorted --")
arr3 = np.array([6, 7, 8, 9])
x = np.searchsorted(arr3, 9)
print(x)

# Search From the Right Side
print("-- Search From the Right Side --")
arr4 = np.array([6, 7, 8, 9])
y = np.searchsorted(arr4, 7, side='right')
print(y)

# Multiple Value

arr5 = np.array([1, 3, 5, 7])
i = np.searchsorted(arr5, [4, 6])
print(i)
