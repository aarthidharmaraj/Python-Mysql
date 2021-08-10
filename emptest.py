from datetime import date
import unittest
import mysql.connector

class TestEmp_manage(unittest.TestCase):

    def mysqlConnection(self):
        con = mysql.connector.connect(user ='root', password ='12345',host='localhost', database ='emp')
        return con

    def Display(self,id):
        query = "SELECT * FROM emp3 WHERE id =%s"
        id= input("Enter User Id to display : ")
        value = id
        con = self.mysqlConnection()
        cur = con.cursor()
        cur.execute(query,(value,))
        details = cur.fetchone()
        con.close()
        details_list  = ["ID :","Name : ","Father Name : ","Post : ","Gender : ","Date Of Birth : ","Contact : "," Salary :"]
        for i in range(0,len(details_list)):
            print(details_list[i],details[i])
        return details

    def test_methods(self):
        result1 = self.Display(1)
        display_result = (1,'abcd','xyzz','Trainer','male','YYYY-MM-DD','8765678987',10000)
        self.assertEqual(result1,display_result)

if __name__ == "__main__":
    unittest.main()