# Python arrays

# Arrays

print("-- Arrays --")
cars = ['Ford', 'Volvo', 'BMW']  # create an array
print(cars)

# Access the Elements of an array:-

print("-- Access the elements form array --")
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
print(fruits[3])

# Length of an array

print("-- Length of an array --")
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
print(len(fruits))

# Looping array elements

print("-- Looping array elements --")
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
for x in fruits:
    print(x)

# Adding array elements

print("-- Adding array elements --")
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
fruits.append("strwberry")
print(fruits)

# Removing array elements

print("-- Removing array elements --")
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
fruits.pop(3)
fruits.remove("kiwi")
print(fruits)
