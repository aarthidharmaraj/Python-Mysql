import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="emp")

my_cursor=mydb.cursor()
#for creating new database

#my_cursor.execute("CREATE DATABASE emp")

#for showing databases

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db[0])

my_cursor.execute("DROP TABLE emp3")
#for creating a table

my_cursor.execute("CREATE TABLE emp3(Id integer NOT NULL,NAME VARCHAR(100),FATHER_NAME VARCHAR(50),PROJECT VARCHAR(50),GENDER VARCHAR(10)NOT NULL,DATE_OF_BIRTH DATE,AGE INTEGER(10),SALARY integer,CONTACT VARCHAR(20),EMAILADDRESS VARCHAR(36) PRIMARY KEY,USER_NAME VARCHAR(50),DOMAIN_NAME VARCHAR(50),PASSWORDD VARCHAR(20) NOT NULL)")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])
my_cursor.execute("DROP TABLE admintable")
my_cursor.execute("CREATE TABLE admintable(ID integer NOT NULL,PASSWORDD VARCHAR(20) NOT NULL)")
sqlInsert="INSERT INTO admintable(ID,PASSWORDD) VALUES(%s,%s)"
record1=("1","admin")
my_cursor.execute(sqlInsert,record1)
mydb.commit()

my_cursor.execute("DROP TABLE usertable")
my_cursor.execute("CREATE TABLE usertable(ID integer NOT NULL,PASSWORDD VARCHAR(20) NOT NULL)")
# sqlInsert="INSERT INTO usertable(ID,PASSWORDD) VALUES(%s,%s)"
# record1=("1","user")
# my_cursor.execute(sqlInsert,record1)
# mydb.commit()