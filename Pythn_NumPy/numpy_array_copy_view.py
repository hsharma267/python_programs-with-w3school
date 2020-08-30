# The Difference between Copy and View
import numpy as np
print("<-- Difference between Copy and View -->")

# Copy:- The copy owns the data and any changes made to the copy will not effect original 					array,and any changes made to the original array will not effect the copy.
# View:- The view does not own data and any changes made to the view will effect the original 				array,and any changes made to the original array will effect the view.

# Copy
print("<-- Copy -->")
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 29
print(arr)
print(x)

# View
print("<-- View -->")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 32
print(arr)
print(x)

# Make changes in the view
print("<-- Make changes in the iew -->")
arr = np.array([7, 5, 3, 1, 5, 9])
x = arr.view()
arr[5] = 93
print(arr)
print(x)

# Check if Array owns its Data
print("<-- Make changes in the iew -->")
arr = np.array([9, 5, 1, 3, 5, 7, 2])
x = arr.view()
y = arr.copy()
print("The copy returns \"NONE\":", y.base)
print("The view returns the original array:", x.base)
