import pandas as pd
import streamlit as st
from mysql.connector import connect
from streamlit_option_menu import option_menu
from datetime import datetime

def login_screen():
    if not st.session_state['login']:
        uid = st.text_input("Enter User ID")
        pwd = st.text_input("Enter Password", type="password")
        btn = st.button("Login")
        if btn:
            mydb = connect(host="localhost", user="root", password="Anoop", database="ems")
            c = mydb.cursor()
            c.execute("SELECT * FROM employee")
            for user in c:
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

mydb = connect(host="localhost", user="root", password="Anoop", database="ems")
cursor = mydb.cursor()

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
            manager_id = cursor.execute(f"SELECT manager_id FROM employee WHERE emp_id='{st.session_state['uid']}'")
            
            # **** check the above query and resolve the issue of "Unread result found" *** #
            
            cursor.execute("INSERT INTO leaves VALUES (%s,%s,%s,%s,%s,%s)",(leave_start_date, leave_end_date, st.session_state['uid'], manager_id, "Pending for approval", leave_reason))
            mydb.commit()
        elif selected == "View Projects":
            projects = pd.read_sql(f"""SELECT E.Emp_ID, E.Emp_Name, P.Project_ID, P.Project_Name, P.Start_Date, P.End_Date, P.Dept_ID, P.Manager_ID, EP.Role_in_Project, EP.Hours_Spent 
                                     FROM employee E JOIN employee_project EP ON E.emp_id = EP.emp_id JOIN projects P ON P.project_id = EP.project_id 
                                     WHERE E.emp_id='{st.session_state['uid']}'""", mydb)
            st.markdown(f"##### Projects Handled by {st.session_state['uname']}: ")
            st.dataframe(projects, use_container_width=True)
        
elif st.session_state['choice'] == "HR":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Human Resource Management", ["View employee", "Add Employee", "Delete Employee", "Update details of the employee", "Add payroll for new employee", "Update payroll for employee", "Add payroll for the month", "Generate & update performance data"], menu_icon="cast")
        st.write(selected)

elif st.session_state['choice'] == "Department Head":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Department Head", ["Update role", "Change department", "Update manager", "Add roles"], menu_icon="cast")
        st.write(selected)

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

st.sidebar.markdown("---")
if st.sidebar.button("Logout"):
    st.session_state['login'] = False
    st.session_state['choice'] = None
    st.sidebar.success("You have been logged out")
