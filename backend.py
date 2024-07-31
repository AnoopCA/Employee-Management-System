import mysql.connector
import datetime

mydb = mysql.connector.connect(host="localhost", user="root", password="Anoop", database="ems")

c = mydb.cursor()

c.execute("CREATE TABLE Employee(Emp_ID VARCHAR(50), Emp_Name VARCHAR(255), Dept_ID VARCHAR(50), Role_ID VARCHAR(50), Contact_No VARCHAR(15), Email VARCHAR(255), Address VARCHAR(255),\
                                 Date_of_Birth DATE, Gender VARCHAR(50), Emergency_Contact VARCHAR(15), Joining_Date DATE, Manager_ID VARCHAR(50), primary key(Emp_ID))")

Emp_ID = input("Enter Employee ID: ")
Emp_Name = input("Enter Employee Name: ")
Dept_ID = input("Enter Department ID: ")
Role_ID = input("Enter Role ID: ")
Contact_No = input("Enter Contact Number: ")
Email = input("Enter Email ID: ")
Address = input("Enter the Address: ")
Date_of_Birth = datetime.datetime.strptime(input("Enter the Date of Birth: "), "%d-%m-%Y").strftime("%Y-%m-%d")
Gender = input("Enter the Gender: ")
Emergency_Contact = input("Enter Emergency Contact number: ")
Joining_Date = datetime.datetime.strptime(input("Enter Joining Date: "), "%d-%m-%Y").strftime("%Y-%m-%d")
Manager_ID = input("Enter Manager ID: ")

c.execute("INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Emp_ID, Emp_Name, Dept_ID, Role_ID, Contact_No, Email, Address, Date_of_Birth,\
                                                                                Gender, Emergency_Contact, Joining_Date, Manager_ID))
c.execute("SELECT * FROM employee")

for i in c:
    print(i)

