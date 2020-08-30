# Numpy Array Iterating

import numpy as np
print("<-- Numpy Array Iteration -->")

# Iterating Arrays
print("-- Iterating Arrays --")
arr = np.array([1, 2, 3, 4, 5])
for x in arr:
    print(x)

# Iterating 2-D Arrays
print("-- Iterating 2-D Arrays --")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr1:
    print(x)

print("-- Example 2-D Arrays --")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr1:
    for y in x:
        print(y)

# Iterating 3-D Arrays
print("-- Iterating 3-D Arrays --")
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr3:
    print(x)

print("-- Example 3-D Arrays --")
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr4:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using nditer()
print("-- Iterating Arrays Using nditer() --")
arr5 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr5):
    print(x)

# Iterating Arrays With Different Data Type
print("-- Iterating Arrays With Different Data Type --")
arr6 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr6, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Iterating Arrays With Different Step
print("-- Iterating Arrays With Different Step --")
arr7 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr7[:, ::2]):
    print(x)

# Enumerated Iteration Using ndenumerate()
print("-- Enumerated Iteration Using ndenumerate() --")
arr8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for idx, x in np.ndenumerate(arr8):
    print(idx, x)
