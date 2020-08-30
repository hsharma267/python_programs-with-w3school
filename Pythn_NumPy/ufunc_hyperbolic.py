# Hyperbolic functions
import numpy as np
print("<-- Hyperbolic functions -->")

print("-- Example --")
x = np.sinh(np.pi/2)
print(x)

print("-- Another Example --")
arr = np.array([np.pi/2, np.pi/2, np.pi/2, np.pi/2, np.pi/2, np.pi/2])
y = np.cosh(arr)
print(y)

# Finding Angles
print("-- Finding Angles --")
b = np.arcsinh(1.0)
print(b)

# Angles of Each Values in Arrays
print("-- Angles of Each Values in Arrays --")
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)
