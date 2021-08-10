# importing mysql connector
import mysql.connector
import re
import admin1
CV=admin1.Check_validation()

def MySQL_Connection():
    from configparser import ConfigParser
    config = ConfigParser()
    file='manage.ini'
    config.read(file)
    data=config['DATAS']
    con = mysql.connector.connect(host=data['host'],user=data['user'], password=data['password'], database=data['database'])
    return con

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

# Function to Promote Employee

class Updatedetails:
    @classmethod
    def Update_Employee(cls):
        Id = int(input("Enter Employ's Id"))   
        if(CV.check_employee(Id) == False):
            print("Employee does not  exists\nTry Again\n")
            US.User_menu()
        else:
            CName=input("Enter Employee's  name to update")
            CFather_name=input("Enter Employee's  Father's name to update")
            CGender=input("Enter Employee's Gender to update ")
            CDateOB=input("Enter Employee's  DateofBirth to update")
            CAge=CV.Calculate_age()
            CContact=input("Enter Employee's  contact number in this format of 10 digits starting with 7/8/9 to update")
            Contact_Check(CContact)

            CEmailAddress=input("Enter the new Email Address in abcd@abcdas.com")
            ECheck=Email_Check(CEmailAddress)

            Cuser_name=ECheck.split('@')[0]
            Cdomain_name=ECheck.split('@')[1]

            sql  = "UPDATE emp3 SET NAME = %s, FATHER_NAME = %s, GENDER = %s, DATE_OF_BIRTH = %s,AGE = %s, CONTACT = %s,EMAILADDRESS = %s ,USER_NAME = %s ,DOMAIN_NAME = %s WHERE id = %s"
            value = (CName,CFather_name,CGender,CDateOB,CAge,CContact,CEmailAddress,Cuser_name,Cdomain_name,Id)
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
            print("Employee Project: ",i[3])
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
        print("Enter 1 to Update Employee")
        print("Enter 2 to Display Employees")
        print("Enter 3 to Exit")
    
        ch = int(input("Enter your Choice "))
        if ch == 1:
            UPD.Update_Employee()
        elif ch == 2:
            UPD.Display_Employees()
        elif ch == 3:
            exit(0)
        else:
            print("Invalid Choice")
            US.User_menu()
UPD=Updatedetails()
US=Usermain()