# importing mysql connector
import mysql.connector
import re
#handling exception
try:
    from empcheck import check_employee
except ImportError as Im:
    print("\n It has troubles to load a module \t and it has a name that cannot be found",Im)
finally:
    print("\n Checked for import error")

con = mysql.connector.connect(host="localhost", user="root", password="12345", database="emp")

#configparser
from configparser import ConfigParser
config = ConfigParser()
file='manage.ini'
config.read(file)

print("\nThe sections in file are",config.sections())
print("\nThe details asked are",list(config['EXAMPLE']))
print("\nThe datas to be given are like",list(config['DATAS']))

with open(file,'w') as f1:
    config.write(f1)

class details:
    @staticmethod
# Function to Add_Employee
    def Add_Employ():
        
        Id = input("Enter Employ Id : ")
        if(check_employee(Id) == True):
            print("Employee aready exists\nTry Again\n")
            m.menu()
         
        else:
            Name = input("Enter Employ Name : ")
            Post = input("Enter Employ Post : ")
            Salary = input("Enter Employ Salary : ")
            Contact=input("Enter the contact number")
        #Checking for validation
        if re.search("[7-9]\w{9}",Contact):
            print("\n",Contact,"is a valid number")

        else:
            print("\n",Contact,"Not a valid number \n Please Enter a number in a valid format")
            m.menu()
        Uname=input("Enter the username")
        # if(re.findall("[\w._%+-]{1,20}@[\w._]{2,20}.[A-Za-z]{2,3}",Emailid)):
        #     print("\n",Emailid, " is a valid emailaddress")
        # else:
        #     print("\n",Emailid,"is not a valid address \n Enter a valid email id")
        #     menu()

        data = (Id, Name, Post, Salary,Contact,Uname)

        # Inserting Employee details in the Employee Table
        sql = 'insert into emp3 values(%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employ Added Successfully")
        m.menu()
 
# Function to Promote Employee
class update:
    @classmethod
    def Update_Employee(cls):
        Id = int(input("Enter Employ's Id"))
            
        # Checking if Employee with given Id Exist or Not
        if(check_employee(Id) == False):
            print("Employee does not  exists\nTry Again\n")
            m.menu()
        else:
            Amount = int(input("Enter increase in Salary"))
            sql = 'select salary from emp3 where id=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            # Fetching Salary of Employee with given Id
            r = c.fetchone()
            t = r[0]+Amount
            sql = 'update emp3 set salary=%s where id=%s'
            d = (t, Id)
            c.execute(sql, d)
            con.commit()
            print("Employe Salary Promoted")
        #Updating the name of employee
            CName = input("Enter the change in name")
            sql = 'select Name from emp3 where id=%s'
            data = (Id,)
            c1 = con.cursor()
            c1.execute(sql, data)
                
            r1=c1.fetchone()
            t1=CName
            sql='update emp3 set Name=%s where id=%s'
            d1=(t1,Id)
            c1.execute(sql,d1)
            con.commit()
            print("\n Employees name is updated")
            m.menu()
    # Function to Remove Employee with given Id
    def Remove_Employ():
        Id = input("Enter Employ Id : ")
        if(check_employee(Id) == False):
            print("Employee does not  exists\nTry Again\n")
            m.menu()
        else:
                
            # Query to Delete Employye from Table
            sql = 'delete from emp3 where id=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)

            con.commit()
            print("Employee Removed")
            m.menu()
 
# Function to Display All Employees from Employee Table
def Display_Employees():
    sql = 'select * from emp3'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employ Id : ", i[0])
        print("Employ Name : ", i[1])
        print("Employ Post : ", i[2])
        print("Employ Salary : ", i[3])
        print("Employee Contcat Number : ",i[4])
        print("Employee Username : ",i[5])
        print("---------------------\
        -----------------------------\
        ------------------------------")
    m.menu()
 
# menu function to display menu
class main:
    def menu(self):
        print("\nWelcome to Employ Management Record")
        print("Enter 1 to Add Employee")
        print("Enter 2 to Remove Employee ")
        print("Enter 3 to Update Employee")
        print("Enter 4 to Display Employees")
        print("Enter 5 to Exit")
    
        ch = int(input("Enter your Choice "))
        if ch == 1:
            c.Add_Employ()
        elif ch == 2:
            u.Remove_Employ()
        elif ch == 3:
            u.Update_Employee()
        elif ch == 4:
            Display_Employees()
        elif ch == 5:
            exit(0)
        else:
            print("Invalid Choice")
            m.menu()
c=details 
u=update
m=main()
m.menu()