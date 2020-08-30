# NumPy Array Reshapping

# Reshapping arrays

import numpy as np
print("<-- Reshapping arrays -->")

# Reshape From 1-D to 2-D
print("-- Reshape from 1-d to 2-d --")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(4, 2)
print(newarr)

# Reshape From 1-D to 3-D
print("-- Reshape from 1-d to 3-d --")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr1 = arr1.reshape(2, 2, 2)
print(newarr1)

# Return Copy or View?
print("<-- Return Copy or View -->")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr2 = arr2.reshape(4, 2).base
print(newarr2)
print(arr2.reshape(4, 2))

# Unknown Dimension
print("<-- Unknown Dimension -->")
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr3 = arr3.reshape(2, 4, -1)
print(newarr3)

# Flattering the arrays
print("<-- Flattering the arrays -->")
arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
newarr4 = arr4.reshape(-1)
print(newarr4)
