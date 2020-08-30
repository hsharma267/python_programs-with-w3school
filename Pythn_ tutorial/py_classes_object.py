# Python Classes/Object

# Create a class
print("-- create a class --")


class MyClass:
    x = 5


myobj = MyClass()
print(myobj.x)

# The __init__ function

print("-- __init__ function --")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Rose", 28)
print(p1.name)
print(p1.age)

# Object Method:

print("-- Object Method --")


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + ".My age is", self.age)


p2 = Person1("Maise", 28)
p2.myfunc()

# self parameter

print("-- self parameter --")


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc1(self):
        print("Hello my name is " + self.name + "."+"My age is", self.age)


p3 = Person2("Sophie", 32)
p3.myfunc1()

# Modify Object properties

print("-- Modify Object properties --")


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc1(self):
        print("Hello,my name is " + self.name + "."+"My age is", self.age)


p4 = Person3("Sophie", 32)
p4.age = 40
p4.myfunc1()

# Delete Object Properties

print("-- Delete Object Properties --")


class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc2(self):
        print("Hello my name is " + self.name + ".")


x = Persons("Emma", 29)
del x.age
x.myfunc2()

# Delete Object


class Persons6:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc2(self):
        print("Hello my name is " + self.name + ".")


x = Persons6("Emma", 29)
del x  # delete the object. It will give u an error message.

# self statement


class Person8:
    pass
