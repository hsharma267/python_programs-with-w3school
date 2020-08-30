# Python condition
print("-- If condition --")
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Elif condition

print("-- Elif condition --")
a = 33
b = 200
if b > a:
    print("b is greater than a ")
elif a == b:
    print("a and b are equal")

# Else condition

print("-- If,elif and else condition --")
a = 200
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b is equal")
else:
    print("a is not greater than b")


print("-- if else condition --")
a = 200
b = 33
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Short hand if condition
print("-- short hand if condition --")
a = 200
b = 53
if a > b:
    print("a is greater than b")

# Short hand if..else condition
print("-- short hand if..else condition --")
a = 200
b = 53
print("a is greater than b") if a > b else print("a is not greater than b")

# This technique is known as ternary operators or conditional expressions.

print("-- short hand if else condition")
a = 53
b = 53
print("a is greater than b") if a > b else print(
    "a and b are equal") if a == b else print("a is not greater than b")

# And

print("-- And condition --")
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")
else:
    print("Both conditions are not true")

# Or
print("-- or condition --")
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions are true")
else:
    print("Both conditions are not true")

# Nested if

x = 40
if x > 20:
    print("x is greather than 20")
    if x > 35:
        print("x is also greater than 35")
    else:
        print("x is not greater than 40")
