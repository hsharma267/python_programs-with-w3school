

# trignometric functions
import numpy as np
print("<-- trignometric functions -->")

print("-- Example --")
x = np.sinh(np.pi/2)
print(x)

print("-- Another Example --")
arr = np.array([np.pi/2, np.pi/2, np.pi/2, np.pi/2, np.pi/2, np.pi/2])
y = np.cosh(arr)
print(y)

# Convert Degree to Radians
print("-- convert degree to Radians --")
arr1 = np.array([90, 180, 270, 360])
a = np.deg2rad(arr1)
print(a)

# Convert Radians to Degree
print("-- Convert Radians to Degree --")
arr2 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
z = np.rad2deg(arr2)
print(z)

# Finding Angles
print("-- Finding Angles --")
b = np.arcsinh(1.0)
print(b)

# Hypotenues
print("-- Hypotenues --")
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)
