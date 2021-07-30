import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="emp")

my_cursor=mydb.cursor()
#for creating new database

#my_cursor.execute("CREATE DATABASE emp")

#for showing databases

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db[0])

#my_cursor.execute("DROP TABLE emp3")
#for creating a table

my_cursor.execute("CREATE TABLE emp3(Id integer NOT NULL,NAME VARCHAR(100),FATHER_NAME VARCHAR(50),POST VARCHAR(50),GENDER VARCHAR(10)NOT NULL,DATE_OF_BIRTH DATE,AGE INTEGER(10),SALARY integer,CONTACT VARCHAR(20),EMAILADDRESS VARCHAR(36) PRIMARY KEY,USER_NAME VARCHAR(50),DOMAIN_NAME VARCHAR(50))")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])