import mysql.connector
from configparser import ConfigParser
config = ConfigParser()
file='manage.ini'
config.read(file)
data=config['DATAS']
con = mysql.connector.connect(host=data['host'],user=data['user'], password=data['password'], database=data['database'])
cur=con.cursor()
import admin1
import user1


def Admin_login():
    id = int(input("Enter User id : "))
    password  = input("Enter Password :")
    cur.execute("SELECT * FROM admintable")
    admin_details = cur.fetchall()
    for record in admin_details:
        print(record)
        record1=cur.fetchone()
        if(record[0]==id and record[1]==password):
            print("Sucessfully Login...")
            AA=admin1.adminmain()
            AA.Admin_main()
        else:
            print("Invalid Admin Login")
            Login_Menu()

def Create_Newuser():
    AD=admin1.add_details()
    AD.Add_Employ()

def User_Login():
    id = int(input("Enter User id : "))
    password  = input("Enter Password :")
    cur.execute("SELECT * FROM usertable")
    user_details = cur.fetchall()
    for record in user_details:
        print(record)
        if(record[0]==id and record[1]==password):
            print("Sucessfully Login...")
            US= user1.Usermain()
            US.User_menu()
    
        else:
            print("Invalid user Login")
            Login_Menu()

def Login_Menu():
    print("\nEnter 1 for Admin login")
    print("\nEnter 2 for User login")
    print("\n Enter 3 for creating new user")

    login_input = int(input("\nEnter  the choice for Login : "))
    if login_input == 1:
        Admin_login()
    elif login_input == 2:
        User_Login()
    elif login_input==3:
        Create_Newuser()
    else:
        Login_Menu()
        
Login_Menu()
