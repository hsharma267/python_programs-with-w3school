# Python collection (Arrays):-

'''
    There are four collection data types in the python programming language:=>

=> List :- is a collection which is ordered and changeable. Allows duplicate members.

=> Tuple :- is a collection which is ordered and unchangeable. Allows duplicate members.

=> Set :- is a collection which is unordered and unindexed. No duplicate members.

=> Dictionary :- is a collection which is ordered,changeable and indexed. No duplicate members.

'''

# List

print("-- Collection Lists --")
thislist = ['apple', 'banana', 'cherry']
print(thislist)

# Access Items

print("-- Access Items --")
thislist = ['apple', 'banana', 'cherry']
print(thislist[2])

# Negative Indexes

print("-- Negative Indexes --")
thislist = ['apple', 'banana', 'cherry']
print(thislist[-2])

# Range of Indexes

print("-- Range of indexes --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist)


thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[:4])


thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:])

# Range of Negative indexes

print("-- Range of Negative indexes --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-6:-2])

# Chnage Item values

print("-- Change Item values --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist[1] = "strawberyy"
print(thislist)

# Loop through a List

print("-- Loop through a List --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
for x in thislist:
    print(x)

# Check if Item Exits

print("-- Check if Item Exits --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
if 'cherry' in thislist:
    print("Yes, \"cherry\" is in the fruits list")

# List Length

print("-- List Length --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mylist = len(thislist)
print(mylist)

# Add Items

print("-- Add Items --\n")

# There two add method of list :- 1.) append() method 2.) insert() method

print("-- append method --")
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.append("banana")
print(thislist)

print("-- insert method --")
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.insert(2, "orange")
print(thislist)

# Remove Item

print("-- Remove Item -- \n")

# There are many methods of Remove Item
'''
    1.) remove() method 2.) pop() method 3.) clear() method

    4.) del keyword

'''

print("--  remove() Method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist.remove("melon")
print(thislist)

print("--  pop() Method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist.pop()
print(thislist)

print("--  del keyword --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
del thislist[6]
print(thislist)

thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
del thislist  # delete keyword can delete the list completely

print("--  clear() Method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist.clear()
print(thislist)

# Copy a list

print("-- Copy a list --\n")

# There are two method of copy list:- 1.) copy() method 2.) list() method

print("-- copy method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mylist = thislist.copy()
print(mylist)

print("-- list method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mylist = list(thislist)
print(mylist)

# Join a list

print("-- join a list --\n")

print("-- join a list using + operator --")

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print("-- Loop through append method --")
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

print("-- extend method --")
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# list() constructor

print("-- list constructor --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mylist = list((thislist))
print(mylist)


# list methods

# In python has a set of built-in method:-
'''
    1.) count() method 2.) index() method 3.) reverse() method 4.) sort() method

    # there are two function :- 1.) reversed() function and iter() function
'''

print("--list method --\n")

print("-- count method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mylist = thislist.count('banana')
print(mylist)

print("-- index method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mylist = thislist.index('mango')
print(mylist)

print("-- reversed method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist.reverse()
print(thislist)

print("-- reversed function --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
mylist = reversed(thislist)
for x in mylist:
    print(x)

print("-- iter function --")
thislist = iter(['apple', 'banana', 'cherry',
                 'orange', 'kiwi', 'melon', 'mango'])
print(next(thislist))
print(next(thislist))
print(next(thislist))


print("-- sort method --")
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist.sort()
print(thislist)
