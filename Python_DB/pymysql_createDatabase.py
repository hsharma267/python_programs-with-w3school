# Python MySQL Create Database

import mysql.connector
print("<-- Python MySQL Create Database -->")
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

mycursor = mydb.cursor()
mycursor.execute("Create Database if exists PythonDb")

# Check if Database Exists
print("-- Check if Database Exists --")

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

mycursor = mydb.cursor()
mycursor.execute("Show Databases")
for x in mycursor:
    print(x)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    db='pythondb'
)
