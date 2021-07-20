import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="db1")

my_cursor=mydb.cursor()
# for creating new database

my_cursor.execute("CREATE DATABASE db1")

#for showing databases

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db[0])

#for creating a table

my_cursor.execute("CREATE TABLE d1(id integer PRIMARY KEY NOT NULL AUTO_INCREMENT,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),EMAIL VARCHAR(150),AGE INTEGER(10),GENDER ENUM('M','F','O')NOT NULL)")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])

#for inserting data into table

sqlInsert="INSERT INTO d1(FIRST_NAME,LAST_NAME,EMAIL,AGE,GENDER) VALUES(%s,%s,%s,%s,%s)"
record1=("Aarthi","Dharmaraj","aarthi@gmail.com",21,"F")
my_cursor.execute(sqlInsert,record1)
record2=("SAI","DHARMARAJ","sai@gmail.com",19,"M")
my_cursor.execute(sqlInsert,record2)
mydb.commit()

#list the datas

my_cursor.execute("select * from user;")
#print(my_cursor.fetchone()) #fetching single data
data=my_cursor.fetchall()
print(data)


#for selecting particular items from table

my_cursor.execute("SELECT id,FIRST_NAME FROM d1 WHERE GENDEr='M' ORDER BY id DESC")
for d in my_cursor:
    print(d)

#for altering items in table

my_cursor.execute("ALTER TABLE d1 ADD COLUMN COURSE VARCHAR(50)NOT NULL")
my_cursor.execute("DESCRIBE d1")
for d in my_cursor:
    print(d)

#for removing or dropping an item from table

my_cursor.execute("ALTER TABLE d1 DROP COURSE")
my_cursor.execute("DESCRIBE d1")
for d in my_cursor:
    print(d)

#for changing the data name

my_cursor.execute("ALTER TABLE d1 CHANGE COURSE course_enrolled VARCHAR(50)")
my_cursor.execute("DESCRIBE d1")
for d in my_cursor:
    print(d)

#deleting particular row

my_cursor.execute("DELETE FROM d1 WHERE AGE >'%d'"%(19))
my_cursor.execute("SELECT * from d1")
print(my_cursor.fetchall()) 