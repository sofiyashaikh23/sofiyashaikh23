import mysql.connector
import streamlit as st

# Establish a connection to MySQL server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sofiya@2323",
    database="curd_db"
)
mycursor = mydb.cursor()

# print("Connection Established")

# Create a Streamlit App
def main():
    st.title("CRUD Operation with MySQL")

    # Display options for CURD operations
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

    # Perform Selected Operation
    if option == "Create":
        st.subheader("Create a Record")
        name = st.text_input("Enter a name")
        email = st.text_input("Enter a email")
        if st.button("Create"):
           sql = "insert into users(name,email) values(%s, %s)"
           val = (name, email)
           mycursor.execute(sql,val) # Execute SQL query
           mydb.commit()    # Commit the changes made in database
           st.success("Record Created Successfully!")


    elif option=="Read":
        st.subheader("Read Record")
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.subheader("Update Record")
        id = st.number_input("Enter ID", min_value=1)
        name = st.text_input("Enter new name")
        email = st.text_input("Enter new email")
        if st.button("Update"):
            sql = "Update users set name=%s, email=%s where id =%s"
            val = (name, email, id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully")

    elif option=="Delete":
        st.subheader("Delete Record")
        id = st.number_input("Enter ID", min_value=1)
        if st.button("Delete"):
            sql = "Delete from users where id=%s"
            val = (id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Successfully")

if __name__ == "__main__":
    main()