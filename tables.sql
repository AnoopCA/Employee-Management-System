CREATE DATABASE ems;
USE ems;

CREATE TABLE Employee(
		Emp_ID VARCHAR(50),
		Emp_Name VARCHAR(255),
		Dept_ID VARCHAR(50),
		Role_ID VARCHAR(50),
		Contact_No VARCHAR(15),
		Email VARCHAR(255),
		Address VARCHAR(255),
		Date_of_Birth DATE,
		Gender VARCHAR(50),
		Emergency_Contact VARCHAR(15),
		Joining_Date DATE,
		Manager_ID VARCHAR(50),
        primary key(Emp_ID)
);
INSERT INTO employee VALUES 
	('E001', 'Anitha', 'HR', 'HRANL', 9123456789, 'anitha@testco.com', '123, ABC Street, Cochin', '1985-07-15', 'Female', 9876543210, '2010-02-15', 'M001'),
	('E002', 'Ravi', 'IT', 'DEV', 7890123456, 'ravi@testco.com', '456, XYZ Avenue, Bangalore', '1990-11-20', 'Male', 8765432109, '2012-06-30', 'M002'),
	('E003', 'Lakshmi', 'FIN', 'ACCT', 7012345678, 'lakshmi@testco.com', '789, DEF Road, Chennai', '1992-01-10', 'Female', 7654321098, '2018-04-10', 'M003'),
    ('E004', 'Rajesh', 'HR', 'HRANL', 7012345679, 'rajesh@testco.com', '123, ABC Street, Bangalore', '1990-05-15', 'Male', 7654321099, '2017-06-12', 'M001'),
	('E005', 'Sunita', 'IT', 'PM', 7012345680, 'sunita@testco.com', '456, XYZ Lane, Hyderabad', '1985-11-20', 'Female', 7654321100, '2019-08-25', 'M002');
SELECT * FROM employee;

CREATE TABLE Department(
		Dept_ID VARCHAR(50),
		Dept_Name VARCHAR(255),
		Manager_ID VARCHAR(50),
		PRIMARY KEY(dept_id)
);
INSERT INTO department VALUES ('HR', 'Human Resource Management', 'M001'),
							  ('IT', 'Information Technology', 'M002'),
                              ('FIN', 'Finance', 'M003'),
                              ('ACC', 'Accounts', 'M004'),
                              ('OPS', 'Operations', 'M005');
SELECT * FROM department;

CREATE TABLE Roles(
		Role_ID VARCHAR(50),
		Role_Name VARCHAR(255),
		Role_Desc VARCHAR(255),
        PRIMARY KEY(role_id)
);
INSERT INTO roles VALUES ( 'HRANL', 'HR Analyst', 'Handles payroll and on-boarding'),
						 ('DEV', 'Developer', 'Handles sofrware development'),
						 ('ACCT', 'Accounts Executive', 'Handles accounts'),
						 ('PM', 'Project Manager', 'Handles projects');
SELECT * FROM roles;

CREATE TABLE Attendance(
		Att_Date DATE,
		Emp_ID VARCHAR(50),
		Attendance_Status VARCHAR(20)
);
INSERT INTO attendance VALUES ('2024-07-18', 'E001', 'Present'),
							  ('2024-07-18', 'E002', 'Present'),
                              ('2024-07-18', 'E003', 'Absent'),
                              ('2024-07-18', 'M001', 'Present'),
                              ('2024-07-18', 'M002', 'Absent');
SELECT * FROM attendance;

CREATE TABLE Leaves(
		Leave_Date DATE,
		Emp_ID VARCHAR(50),
		Approver_ID VARCHAR(50),
		Approval_Status VARCHAR(20)
);
INSERT INTO leaves VALUES ('2024-07-18', 'E001', 'M001', 'Approved'),
						  ('2024-07-15', 'E002', 'M002', 'Rejected'),
                          ('2024-07-13', 'E003', 'M003', 'Approved'),
                          ('2024-07-28', 'E004', 'M001', 'Approved'),
                          ('2024-07-30', 'E005', 'M002', 'Approved');
SELECT * FROM leaves;

CREATE TABLE Payroll(
		Emp_ID VARCHAR(50),
		Month_Year VARCHAR(10),
		Salary INT,
		Deductions INT
);
INSERT INTO payroll VALUES ('E001', 'June 2024', 55000, 1500),
						   ('E002', 'April 2024', 25000, 1000),
                           ('E003', 'May 2024', 30000, 1100),
                           ('E004', 'January 2024', 40000, 1300),
                           ('M001', 'July 2024', 80000, 2500);
SELECT * FROM payroll;

CREATE TABLE Performance (
		Financial_Year VARCHAR(20),
		Emp_ID VARCHAR(50),
		Number_Of_Projects INT,
		Score INT
);
INSERT INTO performance VALUES ('2020-21', 'E001', 4, 6),
							   ('2018-19', 'E002', 7, 8),
                               ('2022-23', 'E001', 8, 9),
                               ('2023-24', 'M001', 14, 8),
                               ('2020-21', 'E002', 2, 3);
SELECT * FROM performance;

CREATE TABLE Projects (
		Project_ID VARCHAR(50),
		Project_Name VARCHAR(255),
		Start_Date DATE,
		End_Date DATE,
		Dept_ID VARCHAR(50),
		Manager_ID VARCHAR(50)
);
INSERT INTO projects VALUES ('PJ001', 'XML Integration', '2020-05-28', '2020-08-18', 'IT', 'M001'),
							('PJ002', 'Database Migration', '2021-01-15', '2021-06-10', 'IT', 'M002'),
							('PJ003', 'Accounts Transfer', '2022-03-22', '2022-09-05', 'ACC', 'M003'),
							('PJ004', 'Network Security', '2023-07-01', '2023-12-15', 'IT', 'M004'),
							('PJ005', 'Booking Transition', '2024-02-10', '2024-07-20', 'OPS', 'M005');
SELECT * FROM projects;

CREATE TABLE Employee_Project(
		Emp_ID VARCHAR(50),
		Project_ID VARCHAR(50),
		Role_in_Project VARCHAR(255),
		Hours_Spent INT
);
INSERT INTO employee_project VALUES ('E005', 'PJ002', 'Database Admin', 250),
									('E002', 'PJ003', 'Project Manager', 250),
                                    ('E003', 'PJ004', 'Network Admin', 250),
                                    ('E001', 'PJ005', 'Operation Manager', 250),
                                    ('E005', 'PJ001', 'Lead Developer', 250);
SELECT * FROM employee_project;