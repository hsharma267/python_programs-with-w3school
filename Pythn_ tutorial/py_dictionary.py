# Python Dictionary

# dictionary :- is a collection of ordered,changeable and indexed. It's written in curly brackets and they have key and values.

print("-- Dictionary -- \n")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict)

# Accessing Items

print("-- Accessing Items --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = thisdict['brand']
print(x)

print("-- get method --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = thisdict.get('model')
print(x)

# Loop through a Dictionary

print("-- Loop through a Dictionary --")

print("-- items name --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
for x in thisdict:
    print(x)

print("-- values name --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
for x in thisdict:
    print(thisdict[x])

print("-- item method --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
for x in thisdict.items():
    print(x)


print("-- value method --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
for x in thisdict.values():
    print(x)

# Check if key Exits

print("-- Check if key Exits --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
if 'model' in thisdict:
    print("Yes \"model\" is one of the keys in the thisdict dictionary")

# Dictionary Length

print("-- Dictionary Length --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(len(thisdict))

# Adding Items:-

print("-- Adding Item --")
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict['color'] = "red"
print(thisdict)

# Removing Items:-

print("-- Removing Item -- \n")

# There are several method in Removing Items
# 1.) pop() method 2.) popitem() method 3.) clear() method 4.) del keyword

print('-- pop method--')
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.pop('model')
print(thisdict)

print('-- popitem method--')
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.popitem()
print(thisdict)

print('-- del keyword--')
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
del thisdict['year']
print(thisdict)

# Copy a dictionary

print("-- Copy a dictionary --")

# There are two method in copy string 1.) copy() method 2.) dict() method

print('-- copy method --')

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = thisdict.copy()
print(x)


print('-- dict method--')
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionary

print("-- Nested Dictionary --\n")
myfamily = {
    "child1": {
        "name": "Praveen",
        "year": 1981
    },
    "child2": {
        "name": "Gagandeep",
        "year": 1988
    },
    "child3": {
        "name": "harish",
        "year": 1991
    }
}
print(myfamily)

print("== Another EX Nested Dictionary")
CSK = {
    "caption": "Dhoni",
    "vice-caption": "Raina"
}
KKR = {
    "caption": "Gambir",
    "vice-caption": "Uttappa"
}
MI = {
    "caption": "Rohit",
    "vice-caption": "Pandya"
}

ipl_team = {
    "CSK": CSK,
    "KKR": KKR,
    "MI": MI
}

print(ipl_team)


# dict constructor

print("-- dict constructor --")
thisdict = dict(brand='Ford', model='Mustang', year=1964)
print(thisdict)


# dict Method

print("-- dict method --\n")

print("-- formkeys method --")
x = ('key1', 'key2', 'key3')
y = 0, 1, 2

thisdict = dict.fromkeys(x, y)
print(thisdict)


print('-- keys method--')
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = thisdict.keys()
print(x)
