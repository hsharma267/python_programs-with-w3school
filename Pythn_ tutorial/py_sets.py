# Python Sets

# Set :- is a collection unordered and unindexed. No duplicate member written in curly brackets.

print("-- Collection Sets --")
thisset = {'apple', 'banana', 'cherry'}
print(thisset)

# Note :- Sets are unordered, so you cannot be sure in which order will appear.

# Access items

# You cannot access in a set by refering index, since sets are unordered the items has no index.

# But you can access through for loop

print('-- Access items through for loop --')
thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

print('Check if \'banana\' is present in the set')
thisset = {'apple', 'banana', 'cherry'}
print("banana" in thisset)


# Change Item

# Once a set is created you cannot change the values but you can add new items.

# Add item

print("-- Add items --")
# There are two method in sets are:- 1.) add() method 2.) update() method

print("-- add method --")
thisset = {'apple', 'banana', 'cherry'}
thisset.add("orange")
print(thisset)

print("-- update method --")
thisset = {'apple', 'banana', 'cherry'}
thisset.update({'orange', 'kiwi', 'melon'})
print(thisset)

# Get Length of a set

print("-- Length method --")
thisset = {'apple', 'banana', 'cherry'}
myset = len(thisset)
print(myset)

# Remove Item

print("-- Remove Item --\n")

# There are several method in Remove method are
# 1.) remove method 2.) discard method 3.) pop method 4.) clear method 5.) del keyword

print("-- remove method--")
thisset = {'apple', 'banana', 'cherry'}
thisset.remove("cherry")
print(thisset)

print("-- discard method --")
thisset = {'apple', 'banana', 'cherry'}
thisset.discard("banana")
print(thisset)

print("-- pop method --")
thisset = {'apple', 'banana', 'cherry'}
thisset.pop()
print(thisset)

print("-- clear method --")
thisset = {'apple', 'banana', 'cherry'}
thisset.clear()
print(thisset)

print("-- del keyword --")
thisset = {'apple', 'banana', 'cherry'}
del thisset
print("delete keyword is delete the whole set")

# Join Two sets

print("-- Join Two sets --\n")
# There are two ways to join the set 1.) union() method 2.) update() method

print("-- union method --")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

print("-- update method --")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# sets constructor

print("-- sets constructor --")
thisset = set(('apple', 'kiwi', 'peach', 'plum'))
print(thisset)

# Sets Method

print("-- sets method --\n")

print("-- difference method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set2.difference(set1)
print(set3)

print("-- difference_update method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft', 'apple'}
set2.difference_update(set1)
print(set2)

print("-- intersection method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.intersection(set2)
print(set3)

print("-- intersection_update method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft', 'apple'}
set1.intersection_update(set2)
print(set1)

print("-- symmetric_difference method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.symmetric_difference(set2)
print(set3)

print("-- symmetric_difference_update method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft', 'apple'}
set1.symmetric_difference_update(set2)
print(set1)


print("-- isdisjoint method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft'}
set3 = set1.isdisjoint(set2)
print(set3)

print("-- issubset method --")
set1 = {'apple', 'cheeku', 'kiwi'}
set2 = {'google', 'microsoft', 'apple', 'cheeku', 'kiwi'}
set3 = set1.issubset(set2)
print(set3)

print("-- issuperset method --")
set1 = {'apple', 'cheeku', 'kiwi', 'microsoft', 'google'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.issuperset(set2)
print(set3)
