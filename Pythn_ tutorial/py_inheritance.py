# Python Inheritance

# Create a Parent Class

print("-- create a parent class --")


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Asa", "Portfield")
x.printname()

# create a child class


print("-- create a child class --")


class Person1:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person1):
    pass


x = Person1("Emma", "Mackey")
x.printname()

# Add the __init__() Function

print("-- Add the __init__() function  in child class --")


class Person3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student1(Person3):
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = Person3("Sara", "Jones")
x.printname()

# Use the super function

print("-- Use the super function --")


class MyPerson:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class MyStudent(MyPerson):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age


x = MyPerson("Maise", "Willams")
x.printname()

# Add properties

print("-- Add Properties --")


class MyPerson2:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class MyStudent1(MyPerson2):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = 28


x = MyPerson2("Nick", "Jones")
x.printname()

# Add Methods

# Add properties

print("-- Add Methods --")


class MPerson3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class MyStudent2(MPerson3):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

    def welcome(self):
        print("Welcome " + self.firstname + " " + self.lastname +
              " I am", self.age, "years old.")


x = MyStudent2("Nick", "Jones", 28)
x.printname()
x.welcome()
