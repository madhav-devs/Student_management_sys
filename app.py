
import streamlit as st
import Database as db

st.title("Student Record Management System")

menu = ["Add Student", "View Students", "Update Student", "Delete Student"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add Student")

    roll = st.number_input("Roll Number", min_value=1)
    name = st.text_input("Name")
    course = st.text_input("Course")
    marks = st.number_input("Marks", min_value=0, max_value=100)

    if st.button("Add"):
        db.add_student(roll, name, course, marks)
        st.success("Student Added Successfully")

elif choice == "View Students":
    st.subheader("Student Records")
    st.dataframe(db.view_students())

elif choice == "Update Student":
    st.subheader("Update Student")

    roll = st.number_input("Roll Number", min_value=1)
    name = st.text_input("New Name")
    course = st.text_input("New Course")
    marks = st.number_input("New Marks", min_value=0, max_value=100)

    if st.button("Update"):
        db.update_student(roll, name, course, marks)
        st.success("Student Updated Successfully")

elif choice == "Delete Student":
    st.subheader("Delete Student")

    roll = st.number_input("Roll Number", min_value=1)

    if st.button("Delete"):
        db.delete_student(roll)
        st.success("Student Deleted Successfully")
