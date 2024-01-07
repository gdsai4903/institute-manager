from tkinter import *
from tkinter import messagebox
import pymysql



class InstituteManager:
    def __init__(self):
        self.DataBaseConnection()
        try:
            query = "select * from usertable"
            rowcount = self.current.execute(query)
            data = self.current.fetchone()
            self.connection.commit()
            if data:
                from login_page import Login_page

                Login_page()
            else:
                from New_admin_page import NewUserPage

                NewUserPage()
        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e))

    def DataBaseConnection(self):
        myhost = "localhost"
        mydb = "institute_manager_db"
        myuser = "root"
        mypassword = ""
        try:
            self.connection = pymysql.connect(
                host=myhost, db=mydb, user=myuser, password=mypassword
            )
            self.current = self.connection.cursor()
        except Exception as e:
            messagebox.showerror(
                "Database Error ", "Error in Database Connection: \n" + str(e)
            )


if __name__ == "__main__":
    InstituteManager()
