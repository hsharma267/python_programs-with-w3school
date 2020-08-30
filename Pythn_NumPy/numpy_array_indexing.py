# Access Array Element
import numpy as np
print("<-- Access Array Element -->")

arr = np.array([1, 2, 3, 4, 5])
print("Access first element:", arr[0])
print("Access second element:", arr[1])

print("Using index add values:", arr[2] + arr[3])

# Access 2-D Arrays
print("-- Access 2-D Arrays --")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print("Access first array print third element:", arr1[0, 2])
print("Access second array print third element:", arr1[1, 2])

# Access 3-D Arrays
print("-- Access 3-D Arrays --")
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Access first array fifth element:", arr2[0, 1, 1])
print("Access second array sixth element:", arr2[1, 1, 2])

# Negative Indexing
print("<-- Negative Indexing -->")
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print("Access first array print last element:", arr1[1, -1])
