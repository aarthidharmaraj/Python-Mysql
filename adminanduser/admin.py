import mysql.connector
from mysql.connector import connection
def mysql_connection():
    from configparser import ConfigParser
    config = ConfigParser()
    file='manage.ini'
    config.read(file)
    data=config['DATAS']
    con = mysql.connector.connect(host=data['host'],user=data['user'], password=data['password'], database=data['database'])
    return con
class adminmain:
    def check_employee(employee_id):
        sql = 'select * from emp3 where id=%s'
        # making cursor buffered to make rowcount method work properly
        con=mysql_connection()
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
    def Remove_Employ():
            Id = input("Enter Employ Id : ")
            if(AD.check_employee(Id) == False):
                print("Employee does not  exists\nTry Again\n")
                AD.Admin_main()
            else: 
                # Query to Delete Employye from Table
                sql = 'delete from emp3 where id=%s'
                data = (Id,)
                con=mysql_connection()
                c = con.cursor()
                c.execute(sql, data)
                con.commit()
                print("Employee Removed")
                AD.Admin_main()
                con.close()

    def Display_Employees():
            sql = 'select * from emp3'
            con=mysql_connection()
            c = con.cursor()
            c.execute(sql)
            r = c.fetchall()
            for i in r:
                print("Employ Id : ",(i[0]))
                print("Employ Name : ", i[1])
                print("Employ Father_name: ",i[2])
                print("Employ Post: ",i[3])
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
            AD.Admin_main()
            con.close()
    def Hike_salary():
        Id = int(input("Enter Employ's Id"))
                
            # Checking if Employee with given Id Exist or Not
        if(AD.check_employee(Id) == False):
            print("Employee does not  exists\nTry Again\n")
            AD.Admin_main()
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
            AD.Admin_main()
            con.close()
    def Admin_main():
        print("\nWelcome Admin to Employ Management Record")
        print("Enter 1 to Remove Employee ")
        print("Enter 2 to Display Employees")
        print("Enter 3 to hike salary")
        print("Enter 4 to Exit")
    
        ch = int(input("Enter your Choice "))
        if ch == 1:
            AD.Remove_Employ()
        elif ch == 2:
            AD.Display_Employees()
        elif ch==3:
            AD.Hike_salary()
        elif ch==4:
            exit(0)
        else:
            print("Invalid Choice")
            AD.Admin_main()
AD=adminmain
AD.Admin_main()