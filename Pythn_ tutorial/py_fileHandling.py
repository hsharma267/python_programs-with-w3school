# File Handling

"""
# Python File Open
# File handling is an important part of any web application.
# Python has several function for creating,reading,updating,and deleting files.

# File Handling

# There are several different methods(modes) for opening a file:-

# 1. "r" - Default value. Open a file for reading,error if the file does not exist
# 2. "a" - Open a file for appending,creates the file if it does not exist
# 3. "w" - Open a file for writing,creates the file if it does not exist
# 4. "x" - Create the specified file, returns an error if the file exist
# 5. "t" - Default value. Text mode
# 6. "b" - Binary mode (eg:-images) """

# Python File Open

print("-- Python File Open --")
f = open("demofile.txt", "r")
print(f.read())

# Read Only Parts of file
print("-- Read Only Parts of file --")
f = open("demofile.txt", "r")
print(f.read(10))

# Read Lines

print("-- Readline method --")
f = open("demofile.txt", "r")
print(f.readline())
print("-- Readlines method --")
f = open("demofile.txt", "r")
print(f.readlines())

# file close

print("-- file close --")
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Python File write

"""
    # 1.) "a" - Append - will append to the end of the file.
    # 2.) "w" - Write - will overwrite any existing contect.
"""

print("-- Append method --")

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

print("-- write method --")

f = open("demofile3.txt", "a")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())
f.close()

# Create a New File

"""
    # "x" - will create a file,return an error if the file exist.
    # "a" - will create a file if the specified file does not exist.
    # "w" - will create a file if the specified file does not exist.
"""

print("-- Create a new file --")
f = open("demo.txt", "x")
f.close()
f = open("demo.txt", "w")
f.write("My name is Harish Kumar. I am 28 years old.")
f.close()
f = open("demo.txt", "r")
print(f.read())
f.close()
