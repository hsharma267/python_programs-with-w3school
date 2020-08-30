
# logs
from math import log
import numpy as np
print("<-- Logs -->")
"""
    . NumPy provides functions to perform log at the base 2,e end 10.
"""

# Log at Base 2
print("-- Log at base 2 --")
arr = np.arange(1, 10)
print(np.log2(arr))

# Log at Base 10
print("-- Log at base 10 --")
arr1 = np.arange(1, 10)
print(np.log10(arr1))

# Natural Log,or Log at Base e
print("-- Natural Log,or Log at Base e")
arr2 = np.arange(1, 10)
print(np.log(arr2))

# Log at Any base
print("-- Log at Any base --")
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
