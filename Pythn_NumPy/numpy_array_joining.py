# Numpy Joining Arrays

import numpy as np
print("<-- Numpy Joining Arrays -->")

# Joining NumPy Arrays
print("-- Joining NumPy Arrays --")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
arr = np.concatenate((arr1, arr2))
print(arr)

print("-- Another Example --")
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])
arr1 = np.concatenate((arr3, arr4), axis=1)
print(arr)

# Joining Arrays Using Stack Functions
print("<-- Joining Arrays Using Stack Function -->")
arr5 = np.array([1, 2, 3, 4, 5])
arr6 = np.array([6, 7, 8, 9, 10])
myarr = np.stack((arr5, arr6), axis=1)
print(myarr)

# Stacking Along Rows
print("<-- Stacking Along Rows -->")
arr7 = np.array([1, 2, 3, 4, 5])
arr8 = np.array([6, 7, 8, 9, 10])
myarr1 = np.hstack((arr7, arr8))
print(myarr1)

# Stacking Along Columns
print("<-- Stacking Along Columns -->")
arr9 = np.array([1, 2, 3, 4, 5])
arr10 = np.array([6, 7, 8, 9, 10])
myarr2 = np.hstack((arr9, arr10))
print(myarr2)

# Stacking Along Height(dept)
print("<-- Stacking Along Height(dept) -->")
arr11 = np.array([1, 2, 3, 4, 5])
arr12 = np.array([6, 7, 8, 9, 10])
myarr3 = np.hstack((arr11, arr12))
print(myarr3)
