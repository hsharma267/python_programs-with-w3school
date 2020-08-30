
# Differences

import numpy as np
print("<-- Differences -->")
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)

print("<-- Example -->")
arr1 = np.array([10, 15, 25, 5])
newarr1 = np.diff(arr, n=2)
print(newarr1)
