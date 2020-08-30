# Python modules

from mymodules import person1, greeting1
import platform
import mymodules as mx
import mymodules

print("-- mymodules --")
mymodules.greeting("Harish")

print("-- another example --")
a = mymodules.person["fname"]
print(a)

print("-- Renaming a module")
mx.greeting("Nick Jones")
a = mx.person["age"]
print(a)

print("-- Built in Module --")
x = platform.system()
print(x)

print("-- Using the dir() function --")
y = dir(platform)
print(y)

print("-- import from module --")
greeting1("Harish")

print("-- another example --")
a = person1["fname"]
print(a)
