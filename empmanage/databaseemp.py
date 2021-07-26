import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database='emp')

my_cursor=mydb.cursor()
#for creating new database

#my_cursor.execute("CREATE DATABASE emp")

#for showing databases

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db[0])

#my_cursor.execute("DROP TABLE emp3")
#for creating a table

my_cursor.execute("CREATE TABLE emp3(Id integer PRIMARY KEY NOT NULL,Name VARCHAR(100),Post VARCHAR(100),Salary integer,Contact VARCHAR(20),Uname VARCHAR(20))")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])