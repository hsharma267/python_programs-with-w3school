# Python String

# 'hello' is same as "Hello"

print("-------------------Assign to a variable---------------------")

# Assign to a variable

x = 5
y = 'Hello world'

print(x, y)

print("---------------------Multiline String ------------------------")

# Multiline String :-

x = """ My name is harish Kumar.
    I have in interset in sports,
    Does it make any difference? """
print(x)

y = '''What brings you here?.
    What did you ,
    I have my own ways. '''
print(y)

print("------------------------String as array-----------------------")

# String as array :-

x = "Hello Friend, You'll enjoy to learn python"
print(x[25])

print("-----------------------Slicing--------------------------")

# Slicing :-

x = " Hello Friend, You'll enjoy to learn python"
print(x[5:45])

print("------------------ Negative Indexing -------------------------")

# Negative Indexing :-

x = "Hello Friend, You'll enjoy to learn python"
print(x[-35:-5])

print("--------------- String Method --------------------------")

# String Method

'''
    1. strip() Method => lstrip() Method => rstrip() Method 
    2. lower() Method => islower() Method
    3. upper() Method => isupper() Method
    4. replace() Method   
    5. split() Method =>split()  Method 
    6. swapcase() Method   
    7. title() Method => istitle() Method
    8. splitlines() Method   
    9. capitalize() Method  
    10. casefold() Method
    11. center() Method
    12. count() Method
    13. endswith() Method
    14. startswith() Method
    15. expandtabs() Method
    16. find() Method => rfind() Method
    17. index() Method => rindex() Method
    18. join() Method
    19. partition() Method => rpartition() Method
    20. format() Method
    21. encode() Method
    22. isalnum() Method
    23. isdecimal() Method
    24. isdigit() Method
    25. isidentifier() Method
    26. isnumeric() Method
    27. isprintable() Method
    28. isspace() Method
    29. ljust() Method =>rjust() Method
    30. zfill() Method
'''

# strip() method

print("-- strip method --")
x = " Python , Djano "
x = x.strip()
print(x)

# lower() method

print("-- lower method -- ")
x = "DJANGO,FLASK"
x = x.lower()
print(x)

# upper() method

print("-- upper method --")
y = "bottle,machine_learning"
y = y.upper()
print(y)

# replace() method

print("-- replace method --")
y = "Jello Jome"
y = y.replace("J", "H")
print(y)

# split() method

print("-- split method --")
z = "Python,language"
z = z.split(",")
print(z)

# swapcase() method

print("-- swapcase method --")
txt = "My name is Harish Sharma."
x = txt.swapcase()
print(x)

# title() method

print("-- title method --")
text = "python is a progrmming language"
x = text.title()
print(x)

# splitlines() method

print("-- splitlines method --")
text = "Python is a \nObject oriented programming language"
x = text.splitlines()
print(x)

# captialize() method

print("-- capitalize method --")
txt = "hello world,welcome to my world"
x = txt.capitalize()
print(x)

# casefold() method

print("-- casefold method --")
text = "HELLO, WELCOME TO MY WORLD"
x = text.casefold()
print(x)

# center(length,character) method

print("-- center methd --")
mychar = "Hello"
x = mychar.center(20)
print(x)

mychar = "Hello"
x = mychar.center(20, "-")
print(x)

# count(value,start,end)

print("-- count method --")
var = "Hello world"
word_count = var.count("world", 5, 15)
print(word_count)

var1 = "I love apple,apple is my favourite fruit"
word_count1 = var1.count("apple", 5, 20)
print(word_count1)

# endswith(value,start,end)

print("-- endswith --")
text = "Hello, Welcome to my world."
var = text.endswith("my world.")
print(var)

text = "Hello, Welcome to my world."
var = text.endswith("my world.", 5, 20)
print(var)

# startswith(value,start,end)

print("-- startswith --")
text = "Hello, Welcome to my world."
var = text.startswith("Hello")
print(var)

text = "Hello, Welcome to my world."
var = text.startswith("Hello", 2, 8)
print(var)

# expandtabs() Method

print("-- expandtabs method --")
x = "H\te\tl\tl\to"
print(x.expandtabs())
print(x.expandtabs(2))
print(x.expandtabs(5))

# find(value,start,end)

print("-- find method --")
text = ("Hello, Welcome to my world")
x = text.find("Welcome")
print(x)

text = ("Hello, Welcome to my world")
x = text.find("e", 5, 10)
print(x)

# index(value,start,end)

print("-- index method --")
text = ("Hello, Welcome to my world")
x = text.index("my")
print(x)

text = ("Hello, Welcome to my world")
x = text.find("q", 5, 10)
x = text.index("m", 5, 20)
print(x)

# join(iterable) Method

print("-- join method -- ")
myset = {'john', 'rose', 'maise'}
x = "#".join(myset)
print(x)

mylist = {'apple', 'kiwi', 'mango'}
myseparator = "||"
x = myseparator.join(mylist)
print(x)

# partition method

print("-- partition method --")
text = "I could eat all bananas all day"
x = text.partition("bananas")
print(x)
x = text.partition(" ")
print(x)

# format(val1,val2,...) Method

print("-- format method --")

x = "For only {price:.2f} dollars"
print(x.format(price=40))

txt1 = "My name is {fname}.I am {age} years old.".format(
    fname="Harish", age=28)
txt2 = "My name is {}.I am {} years old.".format("Harish", 28)
txt3 = "My name is {0}.I am {1} years old.".format("Harish", 28)
print(txt1)
print(txt2)
print(txt3)

# encode(encoding=encoding,error=error) method

print("-- encode method --")
txt = "My name is harish."
x = txt.encode()
print(x)

# isalnum() method

print("-- isalnum method --")
txt = "Python35"
x = txt.isalnum()
print(x)

# isdecimal() method

print("-- isdecimal method --")
txt = "\u0039"  # 0-9 -> 31 to 39
x = txt.isdecimal()
print(x)

# isdigit() method

print("-- isdigit method --")
a = "526814"
x = a.isdigit()
print(x)

# isidentifier() Method --

print("-- isidentifier method--")
x = "_hello_world"
x = x.isidentifier()
print(x)

# islower() Method

print("-- islower method")
x = "hello world"
x = x.islower()
print(x)

# isupper() Method

print("-- isupper method")
x = "HELLO WORLD"
x = x.isupper()
print(x)

# isnumeric() Method

print("-- isnumeric method --")
x = "56584411"
x = x.isnumeric()
print(x)

# isprintable() Method

print("-- isprintable method --")
x = "Hello Are you"
x = x.isprintable()
print(x)

# istitle() Method

print("-- istitle method --")
x = "Hello Are you"
x = x.isprintable()
print(x)

# isspace() method

print("-- isspace method --")
x = "Hello Are you"
x = x.isprintable()
print(x)

# ljust(length,character) Method

x = "Hello"
x = x.ljust(20)
print(x, "are you")

# lstrip(character) Method

print("-- lstrip method --")
x = ",,,,,,aassww  ......Hello "
x = x.lstrip(",asw .")
print(x)

# rfind(value,start,end) Method

print("-- rfind method --")
x = "Hello world, Welcome to my jungle."
x = x.rfind("my jungle.")
print(x)

# rindex(value,start,end) Method

print("-- rindex method --")
x = "Hello world, Welcome to my jungle."
x = x.rindex("to my")
print(x)

# rjust(length,character) Method

print("-- rjust method --")
x = "Hello"
x = x.rjust(20)
print(x, "are you")

# rpartition method

print("-- rpartition method --")
text = "I could eat all bananas all day"
x = text.rpartition("bananas")
print(x)
x = text.rpartition("day")
print(x)

# rsplit() method

print("-- rsplit method --")
z = "Python,language,Java,language"
z = z.split(",")
print(z)

# rstrip(character) Method

print("-- rstrip method --")
x = "Hello,,,,,,aassww  ......"
x = x.rstrip(",asw .")
print(x)

# zfill(len) Method

print("-- zfill() method --")
a = "Hello"
b = "Welcome to my jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
print("--------------- Check String ------------------------")

# Check String

# 1. in
txt = " \n Hello Friend, You'll enjoy to learn python"
x = "enjoy" in txt
print(x)

# 2. not in
txt = " \n Hello Friend, You'll enjoy to learn python"
x = "enjoy" not in txt
print(x)

print("---------------------String Concatenation ----------------------------")

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

x = "Hello"
y = "World"
z = x + " " + y
print(z)

print("-------------------String Format -----------------------")

# String Format

age = 29
text = "My age is {} "
z = text.format(age)
print(z)

price = 50
quantity = 2
text = "I bought {1}kg apples. It's price {0}/- rs. "
z = text.format(price, quantity)
print(z)

print("---------------------Escape Character -------------------------")

# Escape Character

x = "My name is \nHarish Sharma"
print(x)

x = "My name is \tHarish Sharma"
print(x)

x = "My name is \bHarish Sharma"
print(x)

x = "My name is \rHarish Sharma"
print(x)

print("----------------------The End ----------------------")
