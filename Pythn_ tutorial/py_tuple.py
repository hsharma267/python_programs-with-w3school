# Collection Tuple

# Tuple :- is a collection which ordered and unchangeable. Allow duplicate values. In python written with round brackets

# Python Tuple

print("-- Tuple --")
thistuple = ('apple', 'banana', 'mango')
print(thistuple)

# Access tuple items

print("-- Access tuple items --")
thistuple = ('apple', 'banana', 'mango')
print(thistuple[0])

# Negative Indexes

print("-- Negative Indexes --")
thistuple = ('apple', 'banana', 'cherry')
print(thistuple[-2])

# Range of Indexes

print("-- Range of indexes --")
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple)


thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[:4])


thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[2:])

# Range of Negative indexes

print("-- Range of Negative indexes --")
thislist = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thislist[-6:-2])

# Chnage Tuple values

print("-- Change tuple values --")
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
thislist = list(thistuple)
thislist[1] = "strawberyy"
thistuple = tuple(thislist)
print(thistuple)

# Loop through a List

print("-- Loop through a tuple --")
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
for x in thistuple:
    print(x)

# Check if Item Exits

print("-- Check if Item Exits --")
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
if 'cherry' in thistuple:
    print("Yes, \"cherry\" is in the fruits list")

# Tuple Length

print("-- tuple Length --")
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
mytuple = len(thistuple)
print(mytuple)

# Create Tuple with one Item

print("-- create tuple with one item --")

thistuple = ('apple',)
print(type(thistuple))

# Remove Item:-

print("-- Remove Item -- \n")

print("-- del keyword --")
thistuple = ('apple', 'banana', 'mango')
del thistuple  # this will raise an error because the tuple no longer exists

# Join Two Tuples:-

print("-- join a tuple using + operator --")

tuple1 = ['a', 'b', 'c']
tuple2 = [1, 2, 3]
tuple3 = tuple1 + tuple2
print(tuple3)

# Tuple constructor

print("-- tuple constructor --")
tuple1 = tuple(('apple', 'cherry', 'kiwi', 'mango'))
print(tuple1)


# Tuple method
print("-- tuple method --\n")

print("-- count method --")
thistuple = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mytuple = thistuple.count('banana')
print(mytuple)

print("-- index method --")
thistuple = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mytuple = thistuple.index('mango')
print(mytuple)
