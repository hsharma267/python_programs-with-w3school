# Python Try Except

# Exception Handling
print("-- except Handling --")
try:
    print(x)
except:
    print("An exception occurred:")

# Many Exception

print("-- Many Exception --")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else wrong")

# else

print("-- else command --")
try:
    print("hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# finally

print("-- finally --")
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The try except is finished")

# Raise an exception

x = -1
if x < 0:
    raise Exception("Sorry, No number below zero")
