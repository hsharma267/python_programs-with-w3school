import test

mycursor = test.mydb.cursor()
sql = "Create table pytable (name varchar(255), address varchar(255))"
mycursor.execute(sql)
