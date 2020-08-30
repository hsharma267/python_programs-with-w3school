import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    db='pythondb'
)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("create table if exists python")
