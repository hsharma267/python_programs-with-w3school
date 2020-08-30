# Numpy Random

from numpy import random as rand
print("<-- Numpy Random -->")
"""
    Random Introduction:- 
                          Random number does not mean different number everytime. Random means something that cannot be predicted logically.
"""

# Generate Random Number
print("-- Generate Random Number --")
x = rand.randint(100)
print(x)

print("-- Another example --")
x = rand.randint(100, size=(3))
print(x)

print("-- Another example 2 --")
x = rand.randint(100, size=(3, 5))
print(x)

# Generate Random Float
print("-- Generate Random Float --")
y = rand.rand()
print(y)

print("-- Another Example --")
y = rand.rand(3)
print(y)

print("-- Another Example2 --")
y = rand.rand(3, 5)
print(y)

# Generate Random Number From Array
print("-- Generate Random Number From Array --")
z = rand.choice([13, 5, 6, 7, 56, 5])
print(z)

print("-- Another Example --")
z = rand.choice([13, 5, 6, 7, 56, 5], size=(3))
print(z)

print("-- Another Example2 --")
z = rand.choice([13, 5, 6, 7, 56, 5], size=(3, 5))
print(z)
