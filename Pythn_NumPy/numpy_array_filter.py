# NumPy Filter Arrays
import numpy as np
print("<-- NumPy Filter Arrays -->")
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# Creating the Filter Array

print("<-- Creating the Filter Array -->")
arr1 = np.array([41, 42, 43, 44])
filter_arr = []
for elem in arr1:
    if elem > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr1[filter_arr]
print(filter_arr)
print(newarr)

print("<-- Another Example -->")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = []
for elem in arr2:
    if elem % 2 == 0:
        x.append(True)
    else:
        x.append(False)

newarr1 = arr2[x]
print(elem)
print(newarr1)

# Creating Filter Directly From Away

print("-- Creating Filter Directly From Away --")
arr4 = np.array([41, 42, 43, 44])
filter_arr1 = elem > 42

newarr4 = arr4[filter_arr1]
print(filter_arr1)
print(newarr4)

print("<-- Another Example -->")
arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
z = arr5 % 2 == 0

newarr6 = arr5[z]
print(z)
print(newarr6)
