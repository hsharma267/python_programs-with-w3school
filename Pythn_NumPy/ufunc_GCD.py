

"""
    Finding GCD(Greatest Common Denominator):-
                                                The GCD(Greatest comman Denominator), also known as HCF(Highest common Factor) is the biggest number that is a common factor of both of the numbers.
"""

# ufunc Function GCD
import numpy as np
print("<-- ufunc Function GCD -->")
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

# Finding GCD in Arrays
print("<-- Finding GCD in Arrays -->")
arr = np.array([20, 8, 32, 36, 16])
y = np.gcd.reduce(arr)
print(y)
