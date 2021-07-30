import mysql.connector
from configparser import ConfigParser
config = ConfigParser()
file='manage.ini'

config.read(file)
data=config['DATAS']
con = mysql.connector.connect(host=data['host'],user=data['user'], password=data['password'], database=data['database'])
# with open(file,'w') as f1:
#     config.write(f1)

def loginMenu():
    print("\nEnter 1 for Admin Entry of datas")
    print("\nEnter 2 for User Entry of datas")

    login_input = int(input("\nEnter  the choice for Login : "))
    if login_input == 1:
        try:
            import admin
        except ImportError as Im:
            print("\n It has troubles to load a module \t and it has a name that cannot be found",Im)
        finally:
            print("\n Checked for import error of admin module")
    elif login_input == 2:
        try:
            import user
        except ImportError as Im:
            print("\n It has troubles to load a module \t and it has a name that cannot be found",Im)
        finally:
            print("\n Checked for import error of user module")
loginMenu()