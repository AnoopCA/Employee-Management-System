import pandas as pd
import streamlit as st
from mysql.connector import connect
from streamlit_option_menu import option_menu

def login_screen():
    if not st.session_state['login']:
        uid = st.text_input("Enter User ID")
        st.session_state['uid'] = uid
        pwd = st.text_input("Enter Password", type="password")
        btn = st.button("Login")
        if btn:
            mydb = connect(host="localhost", user="root", password="Anoop", database="ems")
            c = mydb.cursor()
            c.execute("SELECT * FROM employee")
            for user in c:
                if user[0]==uid and user[12]==pwd:
                    st.session_state['login'] = True
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

if st.session_state['choice'] == "Employee":
    if login_screen():
        with st.sidebar:
            selected = option_menu("Employee", ["View attendance status", "Mark attendance", "Mark leave", "View individual leaves", "View performance details", "View projects"], menu_icon="cast")

        if selected == "View attendance status":
            st.markdown("##### Attendance Status: ")
            attendance = pd.read_sql(f"SELECT * FROM attendance WHERE emp_id='{st.session_state['uid']}'", mydb)
            st.dataframe(attendance)

        if selected == "View projects":
            projects = pd.read_sql("SELECT * FROM projects", mydb)
            st.dataframe(projects)
        
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

def logout():
    st.session_state['login'] = False
    st.sidebar.success("You have been logged out")

st.sidebar.markdown("---")
if st.sidebar.button("Logout"):
    logout()
