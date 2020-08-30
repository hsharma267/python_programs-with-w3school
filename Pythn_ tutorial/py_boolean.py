# Python Boolean

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 30

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Evaluate Value and Variables

print("-- Evaluate value and Variables --")
print(bool("hello"))
print(bool(25))

x = "Hello"
y = 35
print(bool(x))
print(bool(y))

# Most Values are True

''' 
    bool("harish")             bool(['apple','banana','cherry'])
    bool(123)                  bool({'apple','banana','cherry'})
    bool(" ")                  bool(('apple','banana','cherry'))
    bool(1)
    
'''

# Some Values are False

'''
    bool(False)                  bool([])
    bool(None)                   bool({})
    bool("")                     bool(())
    bool(0)

'''

print("-- __len__ --")


class myclass():
    def myfunction1():
        if __len__(self):
            return 0


myobj = myclass()
print(bool(myobj))

# Function can return a boolean

print("-- Function return boolean value --")


def myfunction():
    return True


print(myfunction())

print("-- Example:- ")


def myfunction1():
    return True


if(myfunction1()):
    print("Yes")
else:
    print("No")

# isinstance() Function

print("-- isinstance() function --")

x = 25
print(isinstance(x, int))
