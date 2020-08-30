
# 1.Create Variable

x = 5
y = "Hello"

# Note. In python, there is no command to declare a variable. if you declare a variable then you assign a value. In python, you don't have initialize the type and can even the value.

# 2. Variable name:-

"""
                1. myvar = "Harish"                4. myVar = "Harish"
                2. _myvar = "Harish"               5. MYVAR = "Harish"
                3. _my_var = "Harish"              6. myvar2 = "Harish"
"""
'''
            you will get error.If you declare variable like this.

                1. my var = "Harish" 2. 2myvar = "Harish" 3. my-var
'''

# 3. Assign a value to the variable:-

x = 5
y = "Hello"

print(x)
print(y)

x, y, z = "Orange", "Apple", "Mango"
print(x, y, z)

x = y = z = "Orange"
print(x, y, z)

# 4. Output Variable

fname = "Harish"
lname = "Sharma"

print("My first name is " + fname + " "+lname)

# 5. Global Variable

languageName = "Awesome"


def mylanNme():
    print("Python is "+languageName)


mylanNme()

myFirstNme = "h_sharma786"


def myName():
    myFirstNme = "hsharma267"
    print("My Name is "+myFirstNme)


myName()
print("My Name is "+myFirstNme)

# 6. Global Keyword


def glblKeywrd():
    global var
    var = "Asa butterfield"


glblKeywrd()
print("Actor name is " + var)

var = "Asa butterfield"


def glblKeywrd1():
    global var
    var = "Ncuti Gatwa"


glblKeywrd1()
print("Actor name is " + var)
