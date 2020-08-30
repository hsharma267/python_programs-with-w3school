# Python Function

# Creating a function

# def my_function():
#print("Hello world")

# Calling a function

print("-- creating & calling a function --")


def my_function():  # creating a function
    print("Hello, world")


my_function()  # calling a function

# Arguments

print("-- passing the arguments in function --")


def my_func(fname):
    print("My name is " + fname)


my_func("Harish")
my_func("Sandy")
my_func("Rose")

# Number of Arguments

print("-- Number of arguments --")


def my_func1(fname, lname):
    print("My name is " + fname + " " + lname)


my_func1("Harish", "Sharma")
my_func1("Rose", "Leslie")

# Aribitrary agruments,* args

print("-- arbitrary agruments --")


def my_fun(*kids):
    print("The child name is " + kids[2])


my_fun("Sandy", "Harish", "Sunny")

# keyword agruments

print("-- keyword agruments --")


def myfunc(child1, child2, child3, child4):
    print("The youngest child name " + child3)


myfunc(child1="Rose", child2="Maise", child3="Sophie", child4="Emme")

# Arbitrary keyword agruments **args

print("-- Arbitrary keyword agruments --")


def my_funct(**kids):
    print("The youngest child lname " + kids["fname"] + " " + kids["lname"])


my_funct(fname="Rose", lname="Leslie")


# Passing lists as an agruments

print("-- Passing lists as an agruments")


def my_frutis(fruitsname):
    for x in fruitsname:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_frutis(fruits)
print("\n")
color = ("red", "green", "blue")
my_frutis(color)

# Return values

print("-- Return values --")


def my_fun2(x):
    return 5*x


print(my_fun2(3))
print(my_fun2(5))
print(my_fun2(7))

# pass statement

print("-- pass statement --")


def my_func2():
    pass

# Recursion


print("-- Recursion --")


def myvalues(value):
    if(value > 0):
        result = value + myvalues(value - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion example result")
myvalues(6)
