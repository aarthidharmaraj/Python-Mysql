import mysql.connector
import re
from datetime import date,datetime
def mysql_connection():
    from configparser import ConfigParser
    config = ConfigParser()
    file='manage.ini'
    config.read(file)
    data=config['DATAS']
    con = mysql.connector.connect(host=data['host'],user=data['user'], password=data['password'], database=data['database'])
    return con
class Check_validation:
    def check_employee(self,employee_id):
         # Query to select all Rows from employee Table
        sql = 'select * from emp3 where id=%s'
        # making cursor buffered to make rowcount method work properly
        con=mysql_connection()
        c = con.cursor(buffered=True)
        data = (employee_id,)
        c.execute(sql, data)

        # rowcount method to find number of rows with given values
        r = c.rowcount

        sql = 'select * from usertable where id=%s'
        data = (employee_id,)
        c.execute(sql, data)
        r1=c.rowcount
        if r == 1 or r1==1:
            return True
        else:
            return False

    def Calculate_age(self,dob):
        DOB=datetime.strptime(dob,"%Y-%m-%d")
        today=date.today()
        age=today.year- DOB.year -((today.month,today.day)<(DOB.month,DOB.day))
        if(age<18):
            print("Employee under age 18 is not allowed\nPlease Try Again")
            exit()
        else:
            print("The Employees Age is calculated")
            return age

def Contact_Check(Contact):
    if re.search("[7-9]\w{9}",Contact):
        print("\n",Contact,"is a valid number")

    else:
        print("\n",Contact,"Not a valid number \n Please Enter a number in a valid format")
        AA.Admin_main()
                
def Email_Check(EmailAddress):
    if(re.findall("[\w._%+-]{1,20}@[\w._]{2,20}.[A-Za-z]{2,3}",EmailAddress)):
        print("\n",EmailAddress, " is a valid emailaddress")
            
    else:
        print("\n",EmailAddress,"is not a valid address \n Enter a valid email id")
        AA.Admin_main()
        return EmailAddress

class add_details:
    @staticmethod
    def Add_Employ():
        
        Id = input("Enter Employ Id : ")
        if(CV.check_employee(Id) == True):
            print("Employee already exists\nTry Again\n")
            AA.Admin_main()
         
        else:
            NAME = input("Enter Employee Name : ")
            FATHER_NAME=input("Enter Employee's Father's Name : ")
            PROJECT=input("Enter Employee's post : ")
            GENDER=input("Enter Employee's  gender : ")
            DATE_OF_BIRTH = input("Enter the Employee's Date of birth in YYYY-MM-DD format : ")
            AGE=CV.Calculate_age(DATE_OF_BIRTH)
            SALARY = input("Enter Employee's  Salary : ")
            CONTACT=input("Enter Employee's contact number in this format of 10 digits starting with 7/8/9")
            
            Contact_Check(CONTACT)

            EMAILADDRESS=input("Enter Employee's EmailId in this format of abcd@abcdefg.xyz ")
            Email_Check(EMAILADDRESS)

            USER_NAME=EMAILADDRESS.split('@')[0]
            DOMAIN_NAME=EMAILADDRESS.split('@')[1]
            PASSWORDD=input("Enter the password")
        data = (Id, NAME,FATHER_NAME,PROJECT,GENDER,DATE_OF_BIRTH,AGE,SALARY,CONTACT,EMAILADDRESS,USER_NAME,DOMAIN_NAME,PASSWORDD)
        data1=(Id,PASSWORDD)
        # Inserting Employee details in the Employee Table
        sql = 'insert into emp3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        sql1='insert into usertable values(%s,%s)'
        con=mysql_connection()
        c = con.cursor()
        c.execute(sql, data)
        c.execute(sql1,data1)
        con.commit()
        print("Employ Added Successfully")
        AA.Admin_main()
        con.close()
class AdminFunctions:
    def Remove_Employ(self):
            Id = input("Enter Employ Id : ")
            if(CV.check_employee(Id) == False):
                print("Employee does not  exists\nTry Again\n")
                AA.Admin_main()
            else: 
                # Query to Delete Employye from Table
                sql = 'delete from emp3 where id=%s'
                data = (Id,)
                con=mysql_connection()
                c = con.cursor()
                c.execute(sql, data)
                con.commit()
                print("Employee Removed")
                AA.Admin_main()
                con.close()

    def Display_Employees(self):
            sql = 'select * from emp3'
            con=mysql_connection()
            c = con.cursor()
            c.execute(sql)
            r = c.fetchall()
            for i in r:
                print("Employ Id : ",(i[0]))
                print("Employ Name : ", i[1])
                print("Employ Father_name: ",i[2])
                print("Employ Project: ",i[3])
                print("Employ Gender: ",i[4])
                print("Employ Date_of_Birth : ", i[5])
                print("Employee Age : ",i[6])
                print("Employ Salary : ", i[7])
                print("Employee Contcat Number : ",i[8])
                print("Employee EmailAddress : ",i[9])
                print("Employee Username : ",i[10])
                print("Employee Domain name :",i[11])
                print("---------------------\
                -----------------------------\
                ------------------------------")
            AA.Admin_main()
            con.close()
    def Hike_salary(self):
        Id = int(input("Enter Employ's Id"))
                
            # Checking if Employee with given Id Exist or Not
        if(CV.check_employee(Id) == False):
            print("Employee does not  exists\nTry Again\n")
            AA.Admin_main()
        else:
            Amount = int(input("Enter increase in Salary"))
            sql = 'select salary from emp3 where id=%s'
            data = (Id,)
            con=mysql_connection()
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
            AA.Admin_main()
            con.close()
class adminmain:
    def Admin_main(self):
        print("\nWelcome Admin to Employ Management Record")
        print("Enter 1 to Add Employee ")
        print("Enter 2 to Remove Employee ")
        print("Enter 3 to Display Employees")
        print("Enter 4 to hike salary")
        print("Enter 5 to Exit")
    
        ch = int(input("Enter your Choice "))
        if ch == 1:
            AD.Add_Employ()
        if ch == 2:
            AF.Remove_Employ()
        elif ch ==3:
            AF.Display_Employees()
        elif ch==4:
            AF.Hike_salary()
        elif ch==5:
            exit(0)
        else:
            print("Invalid Choice")
            AA.Admin_main()
AD=add_details()
AA=adminmain()
AF=AdminFunctions()
CV=Check_validation()