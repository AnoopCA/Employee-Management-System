import streamlit as st

st.title("EMPLOYEE MANAGEMENT SYSTEM")

choice = st.sidebar.selectbox("My Menu", ("Home", "Student", "Admin"))

if choice == "Home":
    st.image("https://static.vecteezy.com/system/resources/previews/005/611/252/non_2x/human-resource-management-selects-a-new-manager-recruiting-the-concept-of-human-resource-management-employee-selection-cv-application-illustration-in-flat-design-free-vector.jpg")
elif choice == "Student":
    st.write("This is the web app dev by Anoop - second")
elif choice == "Admin":
    st.video("https://www.youtube.com/watch?v=AnIk41p9QnA")

