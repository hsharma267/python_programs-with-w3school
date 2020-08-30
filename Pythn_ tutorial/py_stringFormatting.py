# Python String Formatting

# string format()

print("-- string format --")

price = 49
txt = " I have {} dollars."
print(txt.format(price))

# Multiple Values
print("-- Multiple Values --")
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Number
print("-- Index Number")
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print("-- another example --")
age = 36
name = "John"
txt = "His name is {1}.{1} is {0} years old."
print(txt.format(age, name))

# Name Index
print("-- Name Index --")
myorder = "I have a {carname},it's a {model}"
print(myorder.format(carname="Ford", model="BMW"))
