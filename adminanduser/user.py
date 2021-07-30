# importing mysql connector
import mysql.connector
import re

from datetime import date
def MySQL_Connection():
    from configparser import ConfigParser
    config = ConfigParser()
    file='manage.ini'
    config.read(file)
    data=config['DATAS']
    con = mysql.connector.connect(host=data['host'],user=data['user'], password=data['password'], database=data['database'])
    return con

def check_employee(employee_id):
     # Query to select all Rows from employee Table
    sql = 'select * from emp3 where id=%s'
    # making cursor buffered to make rowcount method work properly
    con=MySQL_Connection()
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)

    # rowcount method to find number of rows with given values
    r = c.rowcount
    con.close()
    if r == 1:
        return True
    else:
        return False
def Contact_Check(Contact):
            if re.search("[7-9]\w{9}",Contact):
                print("\n",Contact,"is a valid number")

            else:
                print("\n",Contact,"Not a valid number \n Please Enter a number in a valid format")
                US.User_menu()
def Email_Check(EmailAddress):
    if(re.findall("[\w._%+-]{1,20}@[\w._]{2,20}.[A-Za-z]{2,3}",EmailAddress)):
        print("\n",EmailAddress, " is a valid emailaddress")
        
    else:
        print("\n",EmailAddress,"is not a valid address \n Enter a valid email id")
        US.User_menu()
    return EmailAddress

class Adddetails:
    @staticmethod
# Function to Add_Employee
    def Add_Employ():
        
        Id = input("Enter Employ Id : ")
        if(check_employee(Id) == True):
            print("Employee aready exists\nTry Again\n")
            US.User_menu()
         
        else:
            NAME = input("Enter Employee Name : ")
            FATHER_NAME=input("Enter Employee's Father's Name : ")
            POST=input("Enter Employee's post : ")
            GENDER=input("Enter Employee's  gender : ")
            DATE_OF_BIRTH = input("Enter Employee's  DateofBirth in this format YYYY-MM-DD: ")
            AGE=int(input("Enter the Employee's age "))
            SALARY = input("Enter Employee's  Salary : ")
            CONTACT=input("Enter Employee's contact number in this format of 10 digits starting with 7/8/9")
            Contact_Check(CONTACT)

            EMAILADDRESS=input("Enter Employee's EmailId in this format of abcd@abcdefg.xyz ")
            Email_Check(EMAILADDRESS)

            USER_NAME=EMAILADDRESS.split('@')[0]
            DOMAIN_NAME=EMAILADDRESS.split('@')[1]

        data = (Id, NAME,FATHER_NAME,POST,GENDER, DATE_OF_BIRTH,AGE,SALARY,CONTACT,EMAILADDRESS,USER_NAME,DOMAIN_NAME)

        # Inserting Employee details in the Employee Table
        sql = 'insert into emp3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        con=MySQL_Connection()
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employ Added Successfully")
        US.User_menu()
        con.close()

# Function to Promote Employee

class Updatedetails:
    @classmethod
    def Update_Employee(cls):
        Id = int(input("Enter Employ's Id"))   
        if(check_employee(Id) == False):
            print("Employee does not  exists\nTry Again\n")
            US.User_menu()
        else:
            CName=input("Enter Employee's  name to update")
            CFather_name=input("Enter Employee's  Father's name to update")
            CPost=input("Enter Employee's  post to update")
            CGender=input("Enter Employee's Gender to update ")
            CDateOB=input("Enter Employee's  DateofBirth to update")
            CAge=int(input("Enter the age to update"))
            CContact=input("Enter Employee's  contact number in this format of 10 digits starting with 7/8/9 to update")
            Contact_Check(CContact)

            CEmailAddress=input("Enter the new Email Address in abcd@abcdas.com")
            ECheck=Email_Check(CEmailAddress)

            Cuser_name=ECheck.split('@')[0]
            Cdomain_name=CEmailAddress.split('@')[1]

            sql  = "UPDATE emp3 SET NAME = %s, FATHER_NAME = %s, POST = %s, GENDER = %s, DATE_OF_BIRTH = %s,AGE = %s, CONTACT = %s,EMAILADDRESS = %s ,USER_NAME = %s ,DOMAIN_NAME = %s WHERE id = %s"
            value = (CName,CFather_name,CPost,CGender,CDateOB,CAge,CContact,CEmailAddress,Cuser_name,Cdomain_name,Id)
            con=MySQL_Connection()
            cur=con.cursor()
            cur.execute(sql,value)
            con.commit()

            print("Your Details are Updated Scuceesfully...")
            US.User_menu()
# Function to Display All Employees from Employee Table

    def Display_Employees(self):

        sql = 'select * from emp3'
        con=MySQL_Connection()
        c = con.cursor()
        c.execute(sql)
        r = c.fetchall()
        for i in r:
            print("Employee Id : ",(i[0]))
            print("Employee Name : ", i[1])
            print("Employee Father_name: ",i[2])
            print("Employee Post: ",i[3])
            print("Employee Gender: ",i[4])
            print("Employee DOB : ", i[5])
            print("Employee Age : ",i[6])
            print("Employee Salary : ", i[7])
            print("Employee Contact Number : ",i[8])
            print("Employee EmailAddress : ",i[9])
            print("Employee Username : ",i[10])
            print("Employee Domain name :",i[11])
            print("---------------------\
             -----------------------------\
            ------------------------------")
        US.User_menu()
 
# menu function to display menu
class Usermain:
    def User_menu(self):
        print("\nWelcome to  User Employ Management Record")
        print("Enter 1 to Add Employee")
        print("Enter 2 to Update Employee")
        print("Enter 3 to Display Employees")
        print("Enter 4 to Exit")
    
        ch = int(input("Enter your Choice "))
        if ch == 1:
            ADD.Add_Employ()
        elif ch == 2:
            UPD.Update_Employee()
        elif ch == 3:
            UPD.Display_Employees()
        elif ch == 4:
            exit(0)
        else:
            print("Invalid Choice")
            US.User_menu()
ADD=Adddetails
UPD=Updatedetails()
US=Usermain()
US.User_menu()