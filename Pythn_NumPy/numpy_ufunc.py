# NumPy ufunc :- ufunc stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object

import numpy as np
print("<-- NumPy ufunc -->")

print("-- Example without ufunc --")
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = []
for i, j in zip(x, y):
    z.append(i+j)
print(z)

print("-- Example Using NumPy ufunc --")
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = np.add(x, y)
print(z)

# Create your own function

# How to create our own ufunc :-
"""
  In python, you have to add NumPy unfunc library with the frompyfunc() method.
  The formpyfunc() method takes the following arguments:-
  1. function :- the name of the function.
  2. inputs :- the number of input arguments(arrays)
  3. outputs :- the number of output arrays
"""

print("-- Example --")


def my(x, y):
    return x+y


myobj = np.frompyfunc(my, 2, 1)
print(myobj([1, 2, 3, 4], [5, 6, 7, 8]))

# check if a function is a ufunc
print("-- check if a function is a ufunc --")
print(type(np.add))

# check if a function is a ufunc
print("-- check if a function is a ufunc --")
print(type(np.concatenate))

# Another example
print("-- Another example --")
if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is ufunc")
