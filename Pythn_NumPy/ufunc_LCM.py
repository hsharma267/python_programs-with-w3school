

"""
    Finding LCM(Lowest Common Multiple):-
                                          The Lowest comman multiple is the least number that is comman multiple of both of the numbers.
"""

# ufunc Function LCM
import numpy as np
print("<-- ufunc Function LCM -->")
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

# Finding LCM in Arrays
print("<-- Finding LCM in Arrays -->")
arr = np.array([3, 6, 9])
y = np.lcm.reduce(arr)
print(y)

# Another Example
print("<-- Another Example -->")
arr1 = np.arange(1, 11)
z = np.lcm.reduce(arr1)
print(z)
