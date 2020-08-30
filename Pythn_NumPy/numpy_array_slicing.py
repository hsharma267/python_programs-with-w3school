# Slicing Arrays

import numpy as np
print("<-- Slicing Arrays -->")
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[1:5])
print(arr[2:])
print(arr[:6])

# Negative Slicing
print("<-- Negative Slicing -->")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr1[-6:-2])

# STEP
print("<-- STEP -->")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr2[1:5:3])

print("-- STEP 2-D-- ")
arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Second array print values:", arr3[1, 1:3])
print("Both array print fourth values:", arr3[0:2, 3])
print("Both array print values:", arr3[0:2, 1:4])
