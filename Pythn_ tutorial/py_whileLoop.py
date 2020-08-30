
# Python has two primitive loop commands:->
# 1.) while loop 2.) for loop

# while loop

print("-- while loop --")
i = 1
while i < 6:
    print(i)
    i += 1

# break statement

print("-- break statement --")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue statement

print("-- continue statement --")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement

print("-- else statement --")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
