import mysql.connector
import datetime

mydb = mysql.connector.connect(host="localhost", user="root", password="Anoop", database="ems")

c1 = mydb.cursor()
#c1.execute("select * from employee")
#for r in c1:
#    print(r[1])

#c2 = mydb.cursor()
#c2.execute("select * from leaves")
#for r in c2:
#    print(r[0])

att_time = datetime.date.today().strftime("%Y-%m-%d")
emp_id = input("Enter the Employee ID: ")

c1.execute("INSERT INTO attendance VALUES (%s, %s, %s)", (att_time, emp_id, "Present"))

c1.execute("SELECT * FROM attendance")
for i in c1:
    print(i)