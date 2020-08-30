
# Python Date types

'''
    Text Type : str
    Numeric Type : int,float,complex
    Sequence Types : list,tuple,range
    Mapping Type : dict
    Set Types : set,frozenset
    Boolean Type : bool
    Binary Types:- bytes,bytearray,memoryview
'''

# Setting the Data Type:-

x = "John Snow"
print(type(x))

x = 25
print(type(x))

y = 25.36
print(type(y))

g = 1j
print(type(g))

mylist = ['apple', 'banana', 'cheku']
print(type(mylist))

mytuple = ('apple', 'banana', 'cheku')
print(type(mytuple))

myrange = range(6)
print(type(myrange))

mydict = {'name': 'harish', 'age': 28}
print(type(mydict))

myset = {'apple', 'banana', 'cheeku'}
print(type(myset))

myfrozenset = frozenset({'apple', 'banana', 'cheeku'})
print(type(myfrozenset))

x = True
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

# Setting the specific Data Type:-

print("\n")

x = str("Hello world")
print(type(x))

y = int(35)
print(type(y))

z = float(25.95)
print(type(z))

g = complex(1j)
print(type(g))

mylist = list(('apple', 'Banana', 'Kiwi'))
print(type(mylist))

mytuple = tuple(('mango', 'cheeku', 'kiwi'))
print(type(mytuple))

myrange = range(25)
print(type(myrange))

mydict = dict(name="Harish", age=28)
print(type(mydict))

myset = set(('melon', 'plum', 'peech'))
print(type(myset))

myfrozenset = frozenset(('mango', 'lichi', 'kiwi'))
print(type(myfrozenset))

x = bool(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))
