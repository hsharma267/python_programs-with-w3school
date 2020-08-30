
# lambda

'''
    => A lambda is a small anonymous function.
    => A lambda function can take any number of agruments, but can only have one expression.
        Syntax:- lambda arguments: expression
'''


print("-- lambda function --")

print("lambda using one variable")
def x(a): return a + 10


print(x(5))

print("lambda using two variable")
def xy(a, b): return a+b


print(xy(15, 10))

print("lambda using three variable")
def xyz(a, b, c): return a+b+c


print(xyz(5, 25, 39))

# lamba function

print("-- lambda function --")


def myfun(n):
    return lambda a: a*n


mydoubler = myfun(5)
print(mydoubler(6))

print("  --------------- ")


def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(5)
mytripler = myfunc(6)

print(mydoubler(9))
print(mytripler(32))
