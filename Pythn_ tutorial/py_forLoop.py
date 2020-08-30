

# For loop

print("-- for loop --")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping through a string

print("-- Looping through a string --")
for x in "strawberry":
    print(x)

# break statement

print("-- before output break statement --")
fruits = ["apple", "banana", "cherry", 'orange', 'melon', 'mango']
for x in fruits:
    print(x)
    if x == 'orange':
        break

print("-- after break statement --")
fruits = ["apple", "banana", "cherry", 'orange', 'melon', 'mango']
for x in fruits:
    if x == 'orange':
        break
    print(x)

# continue statement

print("-- continue statement --")
fruits = ["apple", "banana", "cherry", 'orange', 'melon', 'mango']
for x in fruits:
    if x == 'orange':
        continue
    print(x)

# range() function

print("-- range function --")
for x in range(6):
    print(x)

print("-- another example1 --")
for x in range(2, 6):
    print(x)

print("-- another example2 --")
for x in range(2, 30, 3):
    print(x)

# Else in for loop

print("-- else in for loop --")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
else:
    print("Finally finished")

# Nested For loop

print("-- Nested for loop")
fruits = ["apple", "banana", "cherry"]
color = ["red", "green", "blue"]
for x in fruits:
    for y in color:
        print(x, y)

# pass statement

print("-- pass statement --")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    pass
