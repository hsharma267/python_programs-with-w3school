# Shape of an array:->																									The shape of an array is in the number of elements in each dimensions.

# Get the shape of an array
import numpy as np
print("<-- Get the shape of an array -->")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr1 = np.array([1, 2, 3, 4], ndmin=5)
print(arr1)
print("Shape of array:",arr1.shape)
