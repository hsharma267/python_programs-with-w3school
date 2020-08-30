# NumPy Set Operations
import numpy as np
print("-- NumPy Set Operations --")
"""
    . A set in mathematics is a collection of unique elements.
    . Sets are used for operations involving frequent intersection, union and difference operations.
"""

# Create Sets in NumPy:
print("<-- create Sets in NumPy -->")
arr = np.array([1, 2, 3, 4, 5, 6, 2, 5, 6, 7, 5, 2, 4, 9])
x = np.unique(arr)
print(x)

# Finding Union
print("-- Finding Union --")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
arr = np.union1d(arr1, arr2)
print(arr)

# Finding intersection
print("-- Finding intersection --")
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr3, arr4)
print(newarr)

# Finding difference
print("-- Finding difference --")
arr5 = np.array([1, 2, 3, 4])
arr6 = np.array([3, 4, 5, 6])
newarr1 = np.setdiff1d(arr5, arr6)
print(newarr1)

# Finding symmetric_difference
print("-- Finding symmetric_difference --")
arr7 = np.array([1, 2, 3, 4])
arr8 = np.array([3, 4, 5, 6])
newarr2 = np.setxor1d(arr7, arr8)
print(newarr2)
