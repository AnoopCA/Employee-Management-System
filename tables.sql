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
        Password VARCHAR(255),
        primary key(Emp_ID)
);
INSERT INTO employee VALUES 
	('E001', 'Anitha', 'HR', 'HRANL', 9123456789, 'anitha@testco.com', '123, ABC Street, Cochin', '1985-07-15', 'Female', 9876543210, '2010-02-15', 'M001', 'E001'),
	('E002', 'Ravi', 'IT', 'DEV', 7890123456, 'ravi@testco.com', '456, XYZ Avenue, Bangalore', '1990-11-20', 'Male', 8765432109, '2012-06-30', 'M002', 'E002'),
	('E003', 'Lakshmi', 'FIN', 'ACCT', 7012345678, 'lakshmi@testco.com', '789, DEF Road, Chennai', '1992-01-10', 'Female', 7654321098, '2018-04-10', 'M003', 'E003'),
    ('E004', 'Rajesh', 'HR', 'HRANL', 7012345679, 'rajesh@testco.com', '123, ABC Street, Bangalore', '1990-05-15', 'Male', 7654321099, '2017-06-12', 'M001', 'E004'),
	('E005', 'Sunita', 'IT', 'PM', 7012345680, 'sunita@testco.com', '456, XYZ Lane, Hyderabad', '1985-11-20', 'Female', 7654321100, '2019-08-25', 'M002', 'E005'),
	('M001', 'Baiju', 'IT', 'MGR', 7012345680, 'baiju@testco.com', '567, TXM Lane, Telengana', '1985-2-28', 'Male', 8943321100, '2016-08-25', 'M010', 'M001'),
    ('M002', 'Ravi', 'FIN', 'MGR', 8934533253, 'ravi@testco.com', '4567, NY Lane, New York', '1988-6-17', 'Male', 8943334500, '2046-08-25', 'M011', 'M002'),
    ('M003', 'Uthaman', 'OPS', 'HOD', 7983445354, 'uthaman@testco.com', '234, ABC Lane, Kerala', '1996-4-16', 'Male', 8943345100, '2020-08-25', 'M012', 'M003'),
    ('M004', 'Swati', 'LOG', 'HOD', 7898723435, 'swati@testco.com', 'ABC Trrn, Haryana', '1991-6-15', 'Female', 8943324570, '2012-08-25', 'M015', 'M004');
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
		Leave_Start_Date DATE,
        Leave_End_Date DATE,
		Emp_ID VARCHAR(50),
		Approver_ID VARCHAR(50),
		Approval_Status VARCHAR(20),
        Reason_For_leave VARCHAR(255)
);
INSERT INTO leaves VALUES ('2024-08-18', '2024-08-19', 'E001', 'M001', 'Approved', 'headache'),
						  ('2024-08-15', '2024-08-18', 'E002', 'M001', 'Rejected', 'personal function'),
                          ('2024-08-13', '2024-08-14', 'E003', 'M001', 'Pending for Approval', 'marriage'),
                          ('2024-08-28', '2024-08-30', 'E004', 'M001', 'Pending for Approval', 'funeral'),
                          ('2024-08-30', '2024-08-10', 'E005', 'M001', 'Pending for Approval', 'vacation');
SELECT * FROM leaves;

CREATE TABLE Payroll(
		Emp_ID VARCHAR(50),
		Month_Year VARCHAR(50),
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
INSERT INTO performance VALUES ('2022-2023', 'E001', 4, 6),
							   ('2022-2023', 'E002', 7, 8),
                               ('2022-2023', 'E003', 2, 3),
                               ('2022-2023', 'E004', 8, 9),
                               ('2023-2024', 'E001', 2, 4),
							   ('2023-2024', 'E002', 14, 9),
                               ('2023-2024', 'E003', 6, 5),
                               ('2023-2024', 'E004', 12, 8);
SELECT * FROM performance;

CREATE TABLE Projects (
		Project_ID VARCHAR(50),
		Project_Name VARCHAR(255),
		Start_Date DATE,
		End_Date DATE,
		Dept_ID VARCHAR(50),
		Manager_ID VARCHAR(50)
);
INSERT INTO projects VALUES ('PJ001', 'XML Integration', '2023-05-28', '2024-08-18', 'IT', 'E001'),
							('PJ002', 'Database Migration', '2024-01-15', '2025-06-10', 'IT', 'E002'),
							('PJ003', 'Accounts Transfer', '2022-03-22', '2023-09-05', 'ACC', 'E003'),
							('PJ004', 'Network Security', '2023-07-01', '2024-12-15', 'IT', 'E004'),
							('PJ005', 'Booking Transition', '2024-02-10', '2024-07-20', 'OPS', 'E005'),
                            ('PJ006', 'Cloud Integration', '2024-06-10', '2024-12-20', 'IT', 'M001'),
                            ('PJ007', 'XML Integration', '2023-05-28', '2024-08-18', 'IT', 'E001'),
							('PJ008', 'Database Migration', '2022-01-15', '2024-06-10', 'IT', 'E002'),
							('PJ009', 'Accounts Transfer', '2024-03-22', '2025-09-05', 'ACC', 'E002'),
							('PJ010', 'Network Security', '2023-07-01', '2024-12-15', 'IT', 'E002'),
							('PJ011', 'Booking Transition', '2024-02-10', '2024-07-20', 'OPS', 'E003'),
                            ('PJ012', 'Cloud Integration', '2024-06-10', '2024-12-20', 'IT', 'M001');
SELECT * FROM projects;

CREATE TABLE Employee_Project(
		Emp_ID VARCHAR(50),
		Project_ID VARCHAR(50),
		Role_in_Project VARCHAR(255),
		Hours_Spent INT
);
INSERT INTO employee_project VALUES ('E001', 'PJ001', 'Database Admin', 180),
									('E002', 'PJ001', 'Project Manager', 68),
                                    ('E002', 'PJ002', 'Project Manager', 68),
                                    ('E003', 'PJ003', 'Network Admin', 340),
                                    ('E004', 'PJ004', 'Operation Manager', 250),
                                    ('E005', 'PJ005', 'Lead Developer', 125),
                                    ('M001', 'PJ006', 'Cloud Specialt', 118),
                                    ('E001', 'PJ007', 'Database Admin', 180),
									('E002', 'PJ008', 'Project Manager', 68),
                                    ('E003', 'PJ009', 'Network Admin', 340),
                                    ('E004', 'PJ010', 'Operation Manager', 250),
                                    ('E005', 'PJ011', 'Lead Developer', 125),
                                    ('E002', 'PJ012', 'Cloud Specialt', 118);
SELECT * FROM employee_project;
