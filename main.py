import streamlit as st
from mysql.connector import connect

st.title("EMPLOYEE MANAGEMENT SYSTEM")

if 'login' not in st.session_state:
    st.session_state['login'] = False

choice = st.sidebar.selectbox("Select Your Role", ("Please Select", "Employee", "HR", "HOD","Manager", "Project Manager"))

if choice == "Employee":
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
                    break
            if not st.session_state['login']:
                st.write("Incorrect User ID or Password")
    else:
        st.write("Login Successful")
        st.image("https://static.vecteezy.com/system/resources/previews/005/611/252/non_2x/human-resource-management-selects-a-new-manager-recruiting-the-concept-of-human-resource-management-employee-selection-cv-application-illustration-in-flat-design-free-vector.jpg")
        st.video("https://www.youtube.com/watch?v=AnIk41p9QnA")

elif choice == "HR":
    st.write("HR Operations console")
elif choice == "HOD":
    st.write("Placeholder for Department Functions Management")
elif choice == "Manager":
    st.write("Placeholder for the items Manager handles")
elif choice == "Project Manager":
    st.write("Placeholder for project management console")

