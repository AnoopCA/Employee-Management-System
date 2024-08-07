import pandas as pd
import streamlit as st
from mysql.connector import connect
from streamlit_option_menu import option_menu
from datetime import datetime
import time
import calendar

mydb = connect(host="localhost", user="root", password="Anoop", database="ems")
cursor = mydb.cursor()

def popup(message):
    placeholder = st.empty()
    placeholder.success(message)
    time.sleep(2)
    placeholder.empty()
    
def login_screen():
    if not st.session_state['login']:
        uid = st.text_input("Enter User ID")
        pwd = st.text_input("Enter Password", type="password")
        btn = st.button("Login")
        if btn:
            cursor.execute("SELECT * FROM employee")
            for user in cursor:
                if user[0]==uid and user[12]==pwd:
                    st.session_state['login'] = True
                    st.session_state['uid'] = user[0]
                    st.session_state['uname'] = user[1]
                    break
            if not st.session_state['login']:
                st.error("Incorrect ID or Password")
                return False
    else:
        return True

st.title("EMPLOYEE MANAGEMENT SYSTEM")

if 'login' not in st.session_state:
    st.session_state['login'] = False

if not st.session_state['login']:
    st.session_state['choice'] = st.sidebar.selectbox("Select Your Role", ("Employee", "HR", "Department Head", "Manager", "Project Manager"))
else:
    if not st.session_state['choice']:
        st.session_state['choice'] = None

if st.session_state['choice'] == "Employee":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Employee", ["View Attendance Status", "Mark Attendance", "Apply Leave", "View Individual Leaves", "View Performance Details", "View Projects"], menu_icon="cast")

        if selected == "View Attendance Status":
            st.markdown("##### Attendance Status: ")
            att_data = pd.read_sql(f"SELECT * FROM attendance WHERE emp_id='{st.session_state['uid']}'", mydb)
            st.dataframe(att_data)
        
        elif selected == "Mark Attendance":
            st.write("")
            att_stat = pd.read_sql(f"SELECT * FROM attendance WHERE emp_id='{st.session_state['uid']}' and att_date='{datetime.date(datetime.today())}'", mydb)
            if att_stat.empty:
                cursor.execute("INSERT INTO attendance VALUES (%s, %s, 'Present')",(datetime.date(datetime.today()), st.session_state['uid']))
                mydb.commit()
                st.markdown(f"##### Attendance marked for {st.session_state['uname']} for the date {datetime.today().strftime('%d-%m-%Y')}")
            else:
                st.markdown(f"##### Attendance already marked for {st.session_state['uname']} for the date {datetime.today().strftime('%d-%m-%Y')}")

        elif selected == "Apply Leave":
            st.write("")
            st.markdown("##### Apply Leave")
            leave_start_date = st.date_input("Select the start date:")
            leave_end_date = st.date_input("Select the end date:")
            leave_reason = st.text_input("Enter the reason:")
            cursor.execute("SELECT manager_id FROM employee WHERE emp_id=%s", (st.session_state['uid'],))
            manager_id = cursor.fetchall()[0][0]
            if st.button("Apply Leave"):
                cursor.execute("INSERT INTO leaves VALUES (%s,%s,%s,%s,%s,%s)",(leave_start_date, leave_end_date, st.session_state['uid'], manager_id, "Pending for approval", leave_reason))
                popup("Leave Applied Successfully!")
            mydb.commit()

        elif selected == "View Individual Leaves":
            st.write("")
            st.markdown("##### Leaves Applied:")
            leaves = pd.read_sql(f"SELECT * FROM leaves WHERE emp_id='{st.session_state['uid']}'", mydb)
            st.dataframe(leaves, use_container_width=True)
        
        elif selected == "View Performance Details":
            st.write("")
            st.markdown("###### Performance Details:")
            performance = pd.read_sql("SELECT * FROM performance WHERE emp_id='E001'", mydb)
            st.dataframe(performance, use_container_width=True)

        elif selected == "View Projects":
            projects = pd.read_sql(f"""SELECT E.Emp_ID, E.Emp_Name, P.Project_ID, P.Project_Name, P.Start_Date, P.End_Date, P.Dept_ID, P.Manager_ID, EP.Role_in_Project, EP.Hours_Spent 
                                     FROM employee E JOIN employee_project EP ON E.emp_id = EP.emp_id JOIN projects P ON P.project_id = EP.project_id 
                                     WHERE E.emp_id='{st.session_state['uid']}'""", mydb)
            st.markdown(f"##### Projects Handled by {st.session_state['uname']}: ")
            st.dataframe(projects, use_container_width=True)
        
elif st.session_state['choice'] == "HR":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Human Resource Management", ["View Employee", "Add Employee", "Delete Employee", "Update Employee Details", "Generate Monthly Payroll", "Generate & Update Performance Data"], menu_icon="cast")
        
        if selected == "View Employee":
            st.write("")
            emp_id = st.text_input("Provide the Employee ID to get the details:")
            if st.button("Get Employee Details"):
                emp_data = pd.read_sql(f"SELECT * FROM employee WHERE emp_id='{emp_id}'", mydb)
                emp_payroll = pd.read_sql(f"SELECT * FROM payroll WHERE emp_id='{emp_id}'", mydb)
                if emp_data.empty or emp_payroll.empty:
                    st.warning("No details found for the given Employee ID!")
                else:
                    emp_data.drop('Password', axis=1, inplace=True)
                    st.markdown("##### Details for the requested employee:")
                    st.dataframe(emp_data, use_container_width=True)
                    st.markdown("##### Payroll details:")
                    st.dataframe(emp_payroll, use_container_width=True)

        elif selected == "Add Employee":
            Emp_ID = st.text_input("Employee ID")
            Emp_Name = st.text_input("Employee Name")
            Dept_ID = st.text_input("Department ID")
            Role_ID = st.text_input("Role ID")
            Contact_No = st.text_input("Contact Number")
            Email = st.text_input("Email ID")
            Address = st.text_input("Address")
            Date_of_Birth = st.date_input("Date of Birth")
            Gender = st.selectbox("Gender", ["Male", "Female"])
            Emergency_Contact = st.text_input("Emergency Contact Number")
            Joining_Date = st.date_input("Joining Date")
            Manager_ID = st.text_input("Manager ID")
            Password = st.text_input("Password")
            Month_Year = Joining_Date.strftime("%B %Y")
            Salary = st.number_input("Salary")
            Deductions = st.number_input("Deductions")
            if st.button("Save The Data"):
                if not Emp_ID or not Emp_Name or not Dept_ID or not Role_ID or not Contact_No or not Email or not Address or not Gender or not Emergency_Contact or not Manager_ID or not Password or not Month_Year or not Salary or not Deductions:
                    st.warning("Please fill out all the fields.")
                else:
                    cursor.execute("INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Emp_ID, Emp_Name, Dept_ID, Role_ID, Contact_No, Email, Address, Date_of_Birth, Gender, Emergency_Contact, Joining_Date, Manager_ID, Password))
                    mydb.commit()
                    cursor.execute("INSERT INTO payroll VALUES (%s,%s,%s,%s)", (Emp_ID, Month_Year, Salary, Deductions))
                    mydb.commit()

        elif selected == "Delete Employee":
            st.markdown("##### Delete Employee")
            Emp_ID = st.text_input("Enter the Employee ID:")
            if st.button("Delete Employee Data"):
                cursor.execute("SELECT * FROM employee WHERE emp_id=%s",(Emp_ID,))
                match_found = cursor.fetchone()
                if match_found:
                    cursor.execute("DELETE FROM employee WHERE emp_id=%s", (Emp_ID,))
                    mydb.commit()
                    st.success(f"Employee data deleted successfully for the ID {Emp_ID}")
                else:
                    st.error("Employee data not found for the given Employee ID!")

        elif selected == "Update Employee Details":
            Emp_ID = st.text_input("Enter the Employee ID to fetch the data:")
            if st.button("Fetch the data"):
                cursor.execute("SELECT * FROM employee WHERE emp_id=%s",(Emp_ID,))
                emp_data = cursor.fetchone()
                cursor.execute("SELECT * FROM payroll WHERE emp_id=%s",(Emp_ID,))
                emp_payroll = cursor.fetchone()
                if emp_data and emp_payroll:
                    st.session_state['emp_data'] = emp_data
                    st.session_state['emp_payroll'] = emp_payroll
                else:
                    st.error("Employee data not found for the given Employee ID!")
            if 'emp_data' in st.session_state and 'emp_payroll' in st.session_state:
                st.markdown("##### Update Employee Details")
                Emp_ID = st.text_input("Employee ID", value=st.session_state['emp_data'][0])
                Emp_Name = st.text_input("Employee Name", value=st.session_state['emp_data'][1])
                Dept_ID = st.text_input("Department ID", value=st.session_state['emp_data'][2])
                Role_ID = st.text_input("Role ID", value=st.session_state['emp_data'][3])
                Contact_No = st.text_input("Contact Number", value=st.session_state['emp_data'][4])
                Email = st.text_input("Email ID", value=st.session_state['emp_data'][5])
                Address = st.text_input("Address", value=st.session_state['emp_data'][6])
                Date_of_Birth = st.date_input("Date of Birth", value=st.session_state['emp_data'][7])
                Gender = st.selectbox("Gender", ["Male", "Female"], index=0 if st.session_state['emp_data'][8]=="Male" else 1)
                Emergency_Contact = st.text_input("Emergency Contact Number", value=st.session_state['emp_data'][9])
                Joining_Date = st.date_input("Joining Date", value=st.session_state['emp_data'][10])
                Manager_ID = st.text_input("Manager ID", value=st.session_state['emp_data'][11])
                Password = st.session_state['emp_data'][12]
                Month_Year = st.text_input("Month_Year", value=st.session_state['emp_payroll'][1])
                Salary = st.number_input("Salary", value=st.session_state['emp_payroll'][2])
                Deductions = st.number_input("Deductions", value=st.session_state['emp_payroll'][3])
                if st.button("Save Changes"):
                    cursor.execute("UPDATE employee SET Emp_ID=%s,Emp_Name=%s,Dept_ID=%s,Role_ID=%s,Contact_No=%s,Email=%s,Address=%s,Date_of_Birth=%s,Gender=%s,Emergency_Contact=%s,Joining_Date=%s,Manager_ID=%s,Password=%s WHERE emp_id=%s", (Emp_ID,Emp_Name,Dept_ID,Role_ID,Contact_No,Email,Address,Date_of_Birth,Gender,Emergency_Contact,Joining_Date,Manager_ID,Password,Emp_ID))
                    mydb.commit()
                    cursor.execute("UPDATE payroll SET Emp_ID=%s,Month_Year=%s,Salary=%s,Deductions=%s WHERE emp_id=%s", (Emp_ID,Month_Year,Salary,Deductions,Emp_ID))
                    mydb.commit()
                    st.success("Employee details updated successfully!")
                    st.session_state.pop('emp_data', None)
                    st.session_state.pop('emp_payroll', None)
        
        elif selected == "Generate Monthly Payroll":
            st.markdown("##### Previous Payroll:")
            prev_mnth_yr = calendar.month_name[datetime.now().month] + " " + str(datetime.now().year)
            crnt_mnth_yr = calendar.month_name[datetime.now().month + 1] + " " + str(datetime.now().year)
            payroll_prev = pd.read_sql(f"SELECT * FROM payroll WHERE month_year='{prev_mnth_yr}'", mydb)
            st.dataframe(payroll_prev)
            if st.button("Copy previous payroll and generate for current month"):
                cursor.execute("""INSERT INTO payroll (Emp_ID, Month_Year, Salary, Deductions) 
                                  SELECT Emp_ID, %s, Salary, Deductions FROM payroll WHERE Month_Year = %s""", (crnt_mnth_yr, prev_mnth_yr))
                mydb.commit()
                payroll_crnt = pd.read_sql(f"SELECT * FROM payroll WHERE month_year='{crnt_mnth_yr}'", mydb)
                st.dataframe(payroll_crnt)
                st.success(f"Generated payroll for {crnt_mnth_yr} successfully. If any updates are required, please use 'Update Employee Details' option.")

        elif selected == "Generate & Update Performance Data":
            st.write("")
            crnt_mnth = datetime.now().month
            crnt_yr = datetime.now().year
            crnt_fin_yr = str(datetime.now().year) + "-" + str(datetime.now().year + 1)
            if (crnt_mnth < 7) or (crnt_mnth > 9):
                st.warning("The performance review period is July to June and you can generate the performance data only in that period.")
                if st.button("View current performance data"):
                    performance = pd.read_sql(f"SELECT * FROM performance WHERE financial_year='{crnt_fin_yr}'", mydb)
                    st.dataframe(performance)
            else:
                perf_data = pd.read_sql(f"SELECT * FROM performance WHERE financial_year='{crnt_fin_yr}'", mydb)
                if not perf_data.empty:
                    st.markdown(f"##### Performance Data for the Financial Year {crnt_fin_yr}")
                    st.dataframe(perf_data)
                else:
                    cursor.execute("""INSERT INTO performance (Financial_Year, Emp_ID, Number_Of_Projects, Score)
                                    SELECT %s AS Financial_Year, EP.emp_id, COUNT(P.project_id) AS Number_Of_Projects, %s AS Score FROM employee_project EP 
                                    JOIN projects P ON EP.project_id = P.project_id WHERE YEAR(P.start_date)=%s OR YEAR(P.end_date)=%s
                                    GROUP BY EP.emp_id""", (crnt_fin_yr, 5, crnt_yr, crnt_yr))
                    mydb.commit()
                    crnt_perf_data = pd.read_sql(f"SELECT * FROM performance WHERE financial_year='{crnt_fin_yr}'", mydb)
                    st.markdown(f"##### Performance Data has been generated for the Financial Year {crnt_fin_yr} with an average rating of 5 for all employees:")
                    st.dataframe(crnt_perf_data)
                st.markdown(f"##### Update the individual scores below")
                Emp_ID = st.text_input("Emp_ID: ")
                Score = st.text_input("Score: ")
                if st.button("Update the Employee Performance Data"):
                    cursor.execute("UPDATE performance SET Score=%s WHERE emp_id=%s AND financial_year=%s", (Score,Emp_ID,crnt_fin_yr))
                    mydb.commit()
                    st.success("Performance data updated successfully!")

elif st.session_state['choice'] == "Department Head":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Department Head", ["Update Role", "Change Department", "Update Manager", "Add Roles"], menu_icon="cast")
        
        if selected == "Update Role":
            Role_ID = st.text_input("Enter the Role ID to update the details:")
            if st.button("Fetch the Roles Data"):
                cursor.execute("SELECT * FROM roles where role_id=%s", (Role_ID,))
                role_update = cursor.fetchone()
                st.session_state['roles'] = role_update
            if 'roles' in st.session_state and st.session_state['roles']!=None:
                Role_Name = st.text_input("Role Name", value=st.session_state['roles'][1])
                Role_Desc = st.text_input("Role Description", value=st.session_state['roles'][2])
                if st.button("Update the Data"):
                    cursor.execute("UPDATE roles SET role_name=%s, role_desc=%s WHERE role_id=%s", (Role_Name,Role_Desc,Role_ID))
                    mydb.commit()
                    st.success("The role details updated successfully!")
                    st.session_state.pop('roles', None)
            else:
                st.error("The given Role ID is not found!")

        elif selected == "Change Department":
            Emp_ID = st.text_input("Enter the Employee ID to change the Department")
            if st.button("Fetch the details"):
                cursor.execute("SELECT dept_id FROM employee WHERE emp_id=%s", (Emp_ID,))
                Dept_ID = cursor.fetchone()[0]
                if Dept_ID:
                    st.session_state['Emp_ID'] = Emp_ID
                    st.session_state['Dept_ID'] = Dept_ID
            if 'Dept_ID' in st.session_state and st.session_state['Dept_ID']!=None:
                st.text_input("Employee ID:", value=st.session_state['Emp_ID'])
                Dept_ID = st.text_input("Department ID:", value=st.session_state['Dept_ID'])
                if st.button("Update Details"):
                    cursor.execute("UPDATE employee SET dept_id=%s WHERE emp_id=%s", (Dept_ID, st.session_state['Emp_ID']))
                    mydb.commit()
                    st.success("Department has been updated for the employee!")
                    st.session_state.pop('Emp_ID', None)
                    st.session_state.pop('Dept_ID', None)
            else:
                if Emp_ID!="":
                    st.error("The given Employee ID is not found!")

        elif selected == "Update Manager":
            Emp_ID = st.text_input("Enter the Employee ID to change the Manager")
            if st.button("Fetch the details"):
                cursor.execute("SELECT manager_id FROM employee WHERE emp_id=%s", (Emp_ID,))
                Manager_ID = cursor.fetchone()[0]
                if Manager_ID:
                    st.session_state['Emp_ID'] = Emp_ID
                    st.session_state['Manager_ID'] = Manager_ID
            if 'Manager_ID' in st.session_state and st.session_state['Manager_ID']!=None:
                st.text_input("Employee ID:", value=st.session_state['Emp_ID'])
                Manager_ID = st.text_input("Manager ID:", value=st.session_state['Manager_ID'])
                if st.button("Update Details"):
                    cursor.execute("UPDATE employee SET manager_id=%s WHERE emp_id=%s", (Manager_ID, st.session_state['Emp_ID']))
                    mydb.commit()
                    st.success("Manager has been updated for the employee!")
                    st.session_state.pop('Emp_ID', None)
                    st.session_state.pop('Manager_ID', None)
            else:
                if Emp_ID!="":
                    st.error("The given Employee ID is not found!")

                    
elif st.session_state['choice'] == "Manager":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Manager", ["View leaves", "View approval request"], menu_icon="cast")
        st.write(selected)
elif st.session_state['choice'] == "Project Manager":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Project Manager", ["Add project", "Update project details", "Add/update employee project"], menu_icon="cast")
        st.write(selected)

st.session_state['popup'] = False
with st.sidebar:
    st.markdown("<br>" * 4, unsafe_allow_html=True)
    st.sidebar.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Logout"):
            st.session_state['login'] = False
            st.session_state['choice'] = None
            st.session_state['popup'] = True

if st.session_state['popup']:
    popup("You have been logged out!")

mydb.close()
cursor.close()
