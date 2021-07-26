from emp3table import *
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="12345", database="emp")

def check_employee(employee_id):
     # Query to select all Rows from employee Table
    sql = 'select * from emp3 where id=%s'
    # making cursor buffered to make rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)

    # rowcount method to find number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
