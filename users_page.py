from settings import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox, Treeview
from PIL import Image, ImageTk
import pymysql


class Users_page:
    def __init__(self, win):
        # ================== Defining Global variables ==================

        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================

        # ================== Creating window ==================
        self.User_win = Toplevel(win)
        self.User_win.state("zoomed")
        self.User_win.config(background=bg_colour)
        # self.User_win.wm_attributes('-transparentcolor', '#ab23ff')

        self.w = self.User_win.winfo_screenwidth() - 700
        self.h = self.User_win.winfo_screenheight() - 200

        # ================== Creating window ==================

        # ================== Setting up the window ==================
        self.User_win.title("Users")
        self.User_win.geometry("%dx%d+%d+%d" % (self.w, self.h, 300, 50))
        self.W_w = self.User_win.winfo_width()
        self.W_h = self.User_win.winfo_height()

        # Background images =================
        self.image = Image.open("images//i4e2.jpg").resize([1920, 1080])

        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.User_win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # Gtb logo imgage
        self.bgimage = Image.open("images//GTBlogo.jpg")

        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.User_win, image=self.bgimage).place(
            x=1690, y=893
        )
        # Background images =================

        # self.User_win.
        self.heading = Label(
            self.User_win,
            text="USERS",
            background=acent,
            foreground=bg_colour,
            font=heading_font,# relief="raised",
            borderwidth=15,
        )
        self.goback_btn = Button(
            self.User_win,
            text="Bo Back",
            border=2,
            font=button_font,
            foreground=bg_colour,
            background=acent,
            command=lambda: self.User_win.destroy(),
        )
        # ================== Setting up the window ==================

        # ================== Creating Frames ==================
        self.UserInfo = Frame(
            self.User_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=760,
            height=240,
        )

        self.TableFrame = Frame(
            self.User_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=760,
            height=340,
        )
        # ================== Creating Frames ==================

        # =================== User Frame elements ===================

        self.UserFrameHeader = Label(
            self.UserInfo,
            width=50,
            anchor="w",
            text="<<< User Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        self.UserTypeVar = StringVar()
        self.UserTypeLabel = Label(
            self.UserInfo,
            text="User Type :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.UserTypeEntry = Combobox(
            self.UserInfo,
            font=EntryFont,
            textvariable=self.UserTypeVar,
            width=26,
            values=["Admin", "Teacher", "Student"],
            state="readonly",
        )

        self.UserNameLabel = Label(
            self.UserInfo,
            text="Username :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.UserNameEntry = Entry(
            self.UserInfo,
            width=28,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            font=EntryFont,
        )
        self.entry_list.append(self.UserNameEntry)

        self.PasswordLabel = Label(
            self.UserInfo,
            text="Password :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.PasswordEntry = Entry(
            self.UserInfo,
            width=28,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            font=EntryFont,
            show="*",
        )
        self.entry_list.append(self.PasswordEntry)

        # Buttons ============================
        self.FetchUser = Button(
            self.UserInfo,
            text="Fetch (By Name)",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.fetchUser,
        )
        self.SaveUser = Button(
            self.UserInfo,
            text="Save",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.AddUser,
        )
        self.UpdateUser = Button(
            self.UserInfo,
            text="Update",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.updateUser,
        )
        self.DeleteUser = Button(
            self.UserInfo,
            text="Delete",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.DeleteUser,
        )

        # =================== User Frame elements ===================

        # =================== Table Frame Elements ===================

        self.TableFrameHeader = Label(
            self.TableFrame,
            width=50,
            anchor="w",
            text="<<< User Table >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        self.UserTable = Treeview(
            self.TableFrame, columns=["c1", "c2", "c3"], height=11
        )
        self.UserTable.heading("c1", text="Usertype")
        self.UserTable.heading("c2", text="User")
        self.UserTable.heading("c3", text="Duration")
        self.UserTable["show"] = "headings"
        self.UserTable.column("#1", width=245, anchor=CENTER)
        self.UserTable.column("#2", width=245, anchor=CENTER)
        self.UserTable.column("#3", width=245, anchor=CENTER)

        self.UserTable.bind("<ButtonRelease>", lambda e: self.GetPkVaue())

        self.SearchUserNameLabel = Label(
            self.TableFrame,
            text="User Name :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.SearchUserNameEntry = Entry(
            self.TableFrame,
            width=30,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            font=EntryFont,
        )
        self.SearchUserNameEntry.bind("<KeyRelease>", lambda x: self.Search_User())

        self.SearchUser = Button(
            self.TableFrame,
            text="Search",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.Search_User,
        )

        # =================== Table Frame Elements ===================

        # =================== Placing ===================
        # main frame =================
        self.heading.pack(pady=10, fill=X)
        self.goback_btn.place(x=490, y=150)

        f_x = 30
        f_y = 70
        x_diff = 190
        y_diff = 50
        self.UserFrameHeader.place(x=3, y=3)
        self.UserTypeLabel.place(x=f_x, y=f_y)
        self.UserTypeEntry.place(x=f_x + x_diff, y=f_y)
        self.UserNameLabel.place(x=f_x, y=f_y+y_diff)
        self.UserNameEntry.place(x=f_x + x_diff, y=f_y+y_diff)
        self.PasswordLabel.place(x=f_x, y=f_y + y_diff+y_diff)
        self.PasswordEntry.place(x=f_x + x_diff, y=f_y + y_diff+y_diff)

        # buttons
        f_x = 500
        f_y = 40
        x_diff = 235
        y_diff = 50
        self.FetchUser.place(x=f_x, y=f_y)
        self.SaveUser.place(x=f_x, y=f_y + y_diff)
        self.UpdateUser.place(x=f_x, y=f_y + y_diff + y_diff)
        self.DeleteUser.place(
            x=f_x, y=f_y + y_diff + y_diff + y_diff
        )
        self.SearchUser.place(x=f_x, y=35)

        self.UserInfo.pack()

        self.TableFrameHeader.place(x=3, y=3)
        self.SearchUserNameLabel.place(x=10, y=40)
        self.SearchUserNameEntry.place(x=180, y=40)
        self.UserTable.place(x=10, y=80)
        self.TableFrame.pack(pady=10)
        # =================== Placing ===================

        self.DataBaseConnection()
        self.Clear_all()
        self.Search_User()

        self.User_win.mainloop()

    # Database Functions =================

    def DataBaseConnection(self):
        host = "localhost"
        db = "institute_manager_db"
        user = "root"
        password = ""
        try:
            self.connection = pymysql.connect(
                host=host, db=db, user=user, password=password
            )
            self.current = self.connection.cursor()
        except Exception as e:
            messagebox.showerror(
                "!!!Database Error!!!",
                "Couldn't Connect to Database: \nError: " + str(e),
                parent=self.User_win,
            )

    def AddUser(self):
        try:
            query = "insert into usertable values(%s, %s, %s)"
            rowcount = self.current.execute(
                query,
                (
                    self.UserNameEntry.get(),
                    self.PasswordEntry.get(),
                    self.UserTypeEntry.get(),
                ),
            )
            self.connection.commit()

            if rowcount == 1:
                messagebox.showinfo(
                    "Success ", "User Added Successfully", parent=self.User_win
                )
                self.Clear_all()

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.User_win
            )

    def GetPkVaue(self):
        rowID = self.UserTable.focus()

        data = self.UserTable.item(rowID)

        UserData = data["values"]

        pkValue = UserData[0]

        self.fetchUser(pkValue)

    def fetchUser(self, pkValue=None):
        if pkValue == None:
            User = self.UserNameEntry.get()
        else:
            User = pkValue
        try:
            query = "select * from usertable where Username = %s"
            rowcount = self.current.execute(query, (User))
            data = self.current.fetchone()
            self.Clear_all()
            if data:
                self.UserNameEntry.insert(0, data[0])
                self.PasswordEntry.insert(0, data[1])
                self.UserTypeEntry.set(data[2])

            else:
                messagebox.info(
                    "!!Failure!!", "No record Found", parent=self.User_win
                )

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.User_win
            )

    def Search_User(self):
        try:
            query = "select * from usertable where Username like %s"
            rewcount = self.current.execute(
                query, (self.SearchUserNameEntry.get() + "%")
            )
            data = self.current.fetchall()
            self.UserTable.delete(*self.UserTable.get_children())
            if data:
                for row in data:
                    self.UserTable.insert("", END, values=row)
            else:
                messagebox.showinfo(
                    "Failure!!", "No Record Found", parent=self.User_win
                )
        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.User_win
            )

    def updateUser(self):
        try:
            query = "update usertable set Password=%s, UserType=%s where Username=%s"
            rowcount = self.current.execute(query, (self.PasswordEntry.get(), self.UserTypeEntry.get(), self.UserNameEntry.get()))
            self.connection.commit()
            
            if rowcount==1:
                messagebox.showinfo("Success!!", "User Updated Successfully!", parent= self.User_win)
                self.Clear_all()
        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query:\n" + str(e), parent=self.User_win)

    def DeleteUser(self):
        ans = messagebox.askquestion(
            "Confirmation", "Are you sure to delete ?", parent=self.User_win
        )
        if ans == "yes":
            try:
                qry = "delete from usertable where Username=%s"
                rowcount = self.current.execute(qry, (self.UserNameEntry.get()))
                self.connection.commit()
                if rowcount == 1:
                    messagebox.showinfo(
                        "Success ",
                        "User deleted Successfully",
                        parent=self.User_win,
                    )
                    self.Clear_all()

            except Exception as e:
                messagebox.showerror(
                    "Query Error ",
                    "Error in Query: \n" + str(e),
                    parent=self.User_win,
                )

    def Clear_all(self):
        for entry in self.entry_list:
            entry.delete(0, END)
        self.UserTypeEntry.set("Select Value")

        self.Search_User()


if __name__ == "__main__":
    dummy_win = Tk()
    Users_page(dummy_win)
