# Python Scope

print("-- Python Scope --")
print("-- Local Scope --")


def myfunction():
    x = 20
    print(x)


myfunction()

print("-- Function Inside Function --")


def myfunc():
    x = 35

    def abc():
        print(x)

    abc()


myfunc()

# Global Scope

print("-- Global Scope --")
x = 45


def myfun():
    print(x)


myfun()
print(x)

# Naming Variable

print("-- Naming Variable --")
x = 15


def myNum():
    x = 28
    print(x)


myNum()
print(x)

# Global Keyword

print("-- Global Keyword --")
x = 45


def myabc():
    global x
    x = 29
    print(x)


myabc()
print(x)
