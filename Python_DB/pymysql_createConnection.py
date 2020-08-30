# Python MySQL
"""
    . Python can be used in database applications.
    . One of the most popular database in MySQL.
"""

# MySQL Database
"""
    . To be able to experiment with the code examples in this tutorial,you should have install 
         on your computer.
    . You can download a free MySQL database at https:// www. mysql.com/downloads/.

"""

# Install MySQL Driver
"""
    . Python needs a MySQL driver to access the MySQL database.
    . In this tutorial we will use the driver "MySQL Connector".
    . We recommend that you use PIP to install "MySQL Connector".
    . PIP is most likely already installed in your Python environment.
    . Navigate your command line to the location of PIP, and type the following:->
"""

# Download and install "MySQL Connector"
"""
    C:\>cd Users\HarishSharm\AppData\Local\Programs\Python\Python38-32\Scripts>python -m 
          pip install mysql.connector -python 
"""

# Test MySQL Connector
import mysql.connector
print("<-- Test MySQL Connector -->")

# Create Connection

print("-- Create Connection --")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
print(mydb)
