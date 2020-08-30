# Random Data Distribution

from numpy import random as rand
print("<-- Random Data Distribution -->")

"""
    What is Data Distribution:-
                                Data Distribution is a list of all possible values, and how often each value occurs.

    Random Distribution:-
                          A random distribution is a set of random numbers that allows a certain probability density function.

    Probability density function:-
                                    A function that describes a continuous probability i.e. probability of all values an array.
"""

print("-- Examples --")
x = rand.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

print("-- Another Examples --")
x = rand.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
