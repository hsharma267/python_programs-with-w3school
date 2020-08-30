# NumPy Splitting Arrays

import numpy as np

# NumPy Splitting Arrays
print("<-- NumPy Splitting Arrays -->")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.array_split(arr, 3)
print(newarr)

print("<-- Another Example -->")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr1 = np.array_split(arr1, 4)
print(newarr1)

# Split into Arrays

print("-- Split into Arrays --")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr2 = np.array_split(arr2, 3)
print(newarr2[0])
print(newarr2[1])
print(newarr2[2])

# Splitting into 2-D Arrays
print("-- Splitting into 2-D Arrays --")
arr3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr3 = np.array_split(arr3, 3)
print(newarr3)

print("-- Another Example --")
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
                10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr4 = np.array_split(arr4, 3)
print(newarr4)

print("-- Another Example 1 --")
arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
                10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr5 = np.array_split(arr5, 3, axis=1)
print(newarr5)

print("-- NumPy hsplit --")
arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
                10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr7 = np.array_split(arr6, 3, axis=1)
print(newarr7)

# Note - Similar alternates to vstack() and dstack() are available as vsplit() and dsplit()
