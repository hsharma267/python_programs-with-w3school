# Python RegEx

import re

text = "The rain in Spain falls mainly in the sky."
x = re.search("^The.*sky$", text)
if x:
    print("Yes,We have a match!")
else:
    print("No match")


# Built-in Function

'''
    1.)findall              2.) search          3.) split           4.) sub

'''

# Metacharacters

print("-- Meta characters --")

""" 1.) [] :-> Any set of character
    2.) () :-> Capture and group
    3.) {} :-> Exactly the specified number of occurance
    4.)  | :-> Either or
    5.)  . :-> Any characters
    6.)  + :-> One or more occurance
    7.)  * :-> Zero or more occurance
    8.)  ^ :-> starts with
    9.)  $ :-> ends with
    10.) \ :-> Signals a special sequence """

print("-- 1. [] :-any set of characters --")
txt = "The rain in spain"
x = re.findall("[a-m]", txt)
print(x)

print("-- 2. \' :- signal a special sequence --")
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)

print("-- 3. . :- Any character --")
txt = "Hello, world!"
x = re.findall("H...o", txt)
print(x)

print("-- 4. ^ :- Starts with --")
txt = "Hello, world!"
x = re.findall("^Hello", txt)
print(x)

print("-- 5. ^ :- Ends with --")
txt = "Hello, world!"
x = re.findall("world!$", txt)
print(x)

print("-- 6. * :- Zero or more occurance --")
txt = "The rain in spain"
x = re.findall("aix*", txt)
print(x)

print("-- 7. + :- One or more occurance --")
txt = "The rain in spain"
x = re.findall("aix+", txt)
print(x)

print("-- 8. {} :- Exactly the specified number of occurance --")
text = "The rain in Spain falls mainly in the sky."
x = re.findall("al{2}", text)
print(x)

print("-- 9. | :- Either or --")
txt = "The rain in spain"
x = re.findall("rain|falls", txt)
print(x)

# Special sequence

"""
    # 1.) \A            2.) \b              3.) \B            4.)  \d               5.) \D 
    # 6.) \s            7.) \S              8.) \w             9.) \W              10.) \Z
"""

print("-- 1. \A special sequence --")
txt = "The rain in spain"
x = re.findall("\AThe", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 2. \'b special sequence --")
txt = "The rain in spain"
x = re.findall(r"\brain", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

txt = "The rain in spain"
x = re.findall(r"ain\b", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 3. \'B special sequence --")
txt = "The rain in spain"
x = re.findall(r"\Bain", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 4. \d special sequence --")
txt = "The rain in spain"
x = re.findall("\d", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("--  \D special sequence --")
txt = "The rain in spain"
x = re.findall("\D", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 5. \s special sequence --")
txt = "The rain in spain"
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("--  \S special sequence --")
txt = "The rain in spain"
x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 6. \w special sequence --")
txt = "The rain in spain"
x = re.findall("\w", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("--  \W special sequence --")
txt = "The rain in spain"
x = re.findall("\W", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 7. \Z special sequence --")
txt = "The rain in spain"
x = re.findall("spain\Z", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

# Sets

"""
    1.) [arn]       2.) [a-n]               3.) [^arn]          4. [0123] 
    5. [0-9]        6. [0-5][0-9]           7.[a-z][A-z]
"""
print("--- Sets ---")
print("-- 1. [arn] sets --")
txt = "The rain in spain"
x = re.findall("[arn]", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 2. [a-n] sets --")
txt = "The rain in spain"
x = re.findall("[a-n]", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 3. [^arn] sets --")
txt = "The rain in spain"
x = re.findall("[^arn]", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 4. [0123] sets --")
txt = "That will be 59 dollars"
x = re.findall("[0123]", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 5. [0-9] sets --")
txt = "That will be 59 dollars"
x = re.findall("[0-9]", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 6. [0-5][0-9] sets --")
txt = "8 times before 11:45 AM"
x = re.findall("[0-5[[0-9]", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

print("-- 7. [a-zA-Z] sets --")
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
    print("Yes, We have a match")
else:
    print("No match")

# findall function

print("-- findall function --")
txt = "The rain in spain"
c = re.findall("ai", txt)
print(c)

# search function

print("-- search function --")
txt = "The rain in spain"
c = re.search("\s", txt)
print("The first white space character is located in position", c.start())

# split function

print("-- split function --")
txt = "The rain in spain"
c = re.split("\s", txt)
print(c)

# sub function

print("-- sub function --")
txt = "The rain in spain"
c = re.sub("\s", "9", txt, 2)
print(c)

# match Object

print("-- match Object --")
txt = "The rain in spain"
c = re.search("ai", txt)
print(c)

# Match object properties

#    1.) span 2.) string 3. group

# sub properties

print("-- sub properties --")
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# string properties

print("-- string properties --")
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# group properties

print("-- group properties --")
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
