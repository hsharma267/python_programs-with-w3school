
# Python Number 

''' There are three type of numeric types in python
        1. int
        2. float
        3. complex 
'''

x = 25
y = 35.65
z = 1j

print(type(x))
print(type(y))
print(type(z))

print("\n")

# Int

x = 25
y = 3564954922
z = -4654544

print(type(x))
print(type(y))
print(type(z))

print("\n")

# Float

x = 25.35
y = 3564954922.245
z = -4654544.35
g = 35e5
h = 12E4

print(type(x))
print(type(y))
print(type(z))
print(type(g))
print(type(h))

print("\n")
# complex

x = 3+5j
y = 6j
z = -4j

print(type(x))
print(type(y))
print(type(z))

print("\n")
# Type conversion

x = 5
y = 5.9
z = 1j

# convert to int to float

a = float(x)

# convert to float to int

b = float(y)

# convert to int to complex

c = complex(x)

print(a)
print(b)
print(c)

print("\n")

print(type(a))
print(type(b))
print(type(c))

# You cannot convert complex to another type

print("\n")
# Random Number :-

import random 
print(random.randrange(1,10))