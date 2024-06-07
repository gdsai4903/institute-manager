from settings import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox, Treeview
import pymysql
from PIL import Image, ImageTk


class Departments_page:
    def __init__(self, win):
        # ================== Defining Global variables ==================
        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================

        # ================== Creating window ==================
        self.Department_win = Toplevel(win)
        self.Department_win.state("zoomed")
        self.Department_win.config(background=bg_colour)
        # self.Department_win.wm_attributes('-transparentcolor', '#ab23ff')

        self.w = self.Department_win.winfo_screenwidth() - 700
        self.h = self.Department_win.winfo_screenheight() - 200

        # ================== Creating window ==================

        # ================== Setting up the window ==================
        self.Department_win.title("Departments")
        self.Department_win.geometry("%dx%d+%d+%d" % (self.w, self.h, 300, 50))
        self.W_w = self.Department_win.winfo_width()
        self.W_h = self.Department_win.winfo_height()

        # Background images =================
        self.image = Image.open("images//i4e2.jpg").resize([1920, 1080])
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.Department_win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # Gtb logo imgage
        self.bgimage = Image.open("images//GTBlogo.jpg")
        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.Department_win, image=self.bgimage).place(
            x=1690, y=893
        )
        # Background images =================

        # self.Department_win.
        self.heading = Label(
            self.Department_win,
            text="DEPARTMENTS",
            background=acent,
            foreground=bg_colour,
            font=heading_font,
            # relief="raised",
            borderwidth=15,
        )
        self.goback_btn = Button(
            self.Department_win,
            text="Bo Back",
            border=2,
            font=button_font,
            foreground=bg_colour,
            background=acent,
            command=lambda: self.Department_win.destroy(),
        )
        # ================== Setting up the window ==================

        # ================== Creating Frames ==================
        self.DepartmentInfo = Frame(
            self.Department_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=800,
            height=240,
        )

        self.TableFrame = Frame(
            self.Department_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=800,
            height=340,
        )
        # ================== Creating Frames ==================

        # =================== Elements of the Department Frame ===================
        # Department Frame Headers =================
        self.DepartmentFrameHeader = Label(
            self.DepartmentInfo,
            width=50,
            anchor="w",
            text="<<< Department Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        self.DepartmentNameLabel = Label(
            self.DepartmentInfo,
            text="Department Name :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.DepartmentNameEntry = Entry(
            self.DepartmentInfo,
            width=33,
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
        self.entry_list.append(self.DepartmentNameEntry)

        self.DepartmentHeadLabel = Label(
            self.DepartmentInfo,
            text="Department Head :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.DepartmentHeadEntry = Entry(
            self.DepartmentInfo,
            width=33,
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
        self.entry_list.append(self.DepartmentHeadEntry)

        # Buttons ============================
        self.FetchDepartment = Button(
            self.DepartmentInfo,
            text="Fetch\n(By Department Name)",
            width=20,
            height=4,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.fetchDepartment,
        )
        self.SaveDepartment = Button(
            self.DepartmentInfo,
            text="Save",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.AddDepartment,
        )
        self.UpdateDepartment = Button(
            self.DepartmentInfo,
            text="Update",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.updateDepartment,
        )
        self.DeleteDepartment = Button(
            self.DepartmentInfo,
            text="Delete",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.DeleteDepartment,
        )

        # =================== Elements of the Department Frame ===================

        # =================== Elements of the Table Frame ===================

        self.DepartmentTableHeader = Label(
            self.TableFrame,
            width=50,
            anchor="w",
            text="<<< Department Table >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        self.SearchDepartmentHeadLabel = Label(
            self.TableFrame,
            text="Department Head :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.SearchDepartmentHeadEntry = Entry(
            self.TableFrame,
            width=33,
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
        self.SearchDepartmentHeadEntry.bind("<KeyRelease>", lambda x: self.Search_department())
        self.entry_list.append(self.SearchDepartmentHeadEntry)

        self.SearchDepartment = Button(
            self.TableFrame,
            text="Search (By head)",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.Search_department,
        )

        # Table ==================

        # ------------ table ---------------------------
        self.DepartmentTable = Treeview(
            self.TableFrame,
            columns=["c1", "c2"],
            height=10,
        )

        self.DepartmentTable.heading("c1", text="Department")
        self.DepartmentTable.heading("c2", text="Head")

        self.DepartmentTable["show"] = "headings"
        self.DepartmentTable.column("#1", width=390, anchor="center")
        self.DepartmentTable.column("#2", width=390, anchor="center")

        self.DepartmentTable.bind("<ButtonRelease>", lambda e: self.GetPkVaue())
        # =================== Elements of the Table Frame ===================

        # =================== Placing ===================

        # Frames =================
        self.heading.pack(pady=10, fill=X)
        self.DepartmentInfo.pack()
        self.TableFrame.pack(pady=5)
        self.goback_btn.place(x=470, y=150)
        # Frames =================

        # Departments =================
        self.DepartmentFrameHeader.place(x=3, y=3)

        f_x = 10
        f_y = 60
        x_diff = 190
        y_diff = 60
        self.DepartmentNameLabel.place(x=f_x, y=f_y)
        self.DepartmentNameEntry.place(x=f_x + x_diff, y=f_y)
        self.DepartmentHeadLabel.place(x=f_x, y=f_y + y_diff)
        self.DepartmentHeadEntry.place(x=f_x + x_diff, y=f_y + y_diff)

        # buttons
        f_x = 35
        f_y = 60
        x_diff = 260
        y_diff = 60
        self.SaveDepartment.place(x=f_x, y=f_y + y_diff + y_diff)
        self.UpdateDepartment.place(x=f_x + x_diff, y=f_y + y_diff + y_diff)
        self.DeleteDepartment.place(x=f_x + x_diff + x_diff, y=f_y + y_diff + y_diff)
        self.FetchDepartment.place(x=f_x + x_diff + x_diff, y=f_y)
        self.SearchDepartment.place(x=f_x + x_diff + x_diff, y=f_y - 15)

        f_x = 10
        f_y = 50
        x_diff = 190
        y_diff = 60
        self.DepartmentTableHeader.place(x=3, y=3)
        self.SearchDepartmentHeadLabel.place(x=f_x, y=f_y)
        self.SearchDepartmentHeadEntry.place(x=f_x + x_diff, y=f_y)
        self.DepartmentTable.place(x=f_x - 1, y=f_y + y_diff - 10)

        # =================== Placing ===================

        self.DataBaseConnection()
        self.Clear_all()
        self.Search_department()

        self.Department_win.mainloop()

    # Database Functions =================

    def DataBaseConnection(self):
        host = "localhost"
        db = "institute_manager_db"
        user = "root"
        password = sql_pass
        try:
            self.connection = pymysql.connect(
                host=host, db=db, user=user, password=password
            )
            self.current = self.connection.cursor()
        except Exception as e:
            messagebox.showerror(
                "!!!Database Error!!!",
                "Couldn't Connect to Database: \nError: " + str(e),
                parent=self.Student_win,
            )

    def AddDepartment(self):
        try:
            query = "insert into departments_table values(%s,%s)"
            rowcount = self.current.execute(
                query,
                (
                    self.DepartmentNameEntry.get(),
                    self.DepartmentHeadEntry.get(),
                ),
            )
            self.connection.commit()

            if rowcount == 1:
                messagebox.showinfo(
                    "Success ",
                    "Department Added Successfully",
                    parent=self.Department_win,
                )
                self.Clear_all()

        except Exception as e:
            messagebox.showerror(
                "Query Error ",
                "Error in Query: \n" + str(e),
                parent=self.Department_win,
            )

    def GetPkVaue(self):
        rowID = self.DepartmentTable.focus()

        data = self.DepartmentTable.item(rowID)

        DepartmentData = data["values"]

        pkValue = DepartmentData[0]

        self.fetchDepartment(pkValue)

    def fetchDepartment(self, pkValue=None):
        if pkValue == None:
            dep_name = self.DepartmentNameEntry.get()
        else:
            dep_name = pkValue
        try:
            query = "select * from departments_table where Department_Name = %s"
            rowcount = self.current.execute(query, (dep_name))
            data = self.current.fetchone()
            self.Clear_all()
            if data:
                self.DepartmentNameEntry.insert(0, data[0])
                self.DepartmentHeadEntry.insert(0, data[1])

            else:
                messagebox.info(
                    "!!Failure!!", "No record Found", parent=self.Department_win.win
                )

        except Exception as e:
            messagebox.showerror(
                "Query Error ",
                "Error in Query: \n" + str(e),
                parent=self.Department_win,
            )

    def Search_department(self):
        try:
            query = "select * from departments_table where Department_Head like %s"
            rewcount = self.current.execute(
                query, (self.SearchDepartmentHeadEntry.get() + "%")
            )
            data = self.current.fetchall()
            self.DepartmentTable.delete(*self.DepartmentTable.get_children())
            if data:
                for row in data:
                    self.DepartmentTable.insert("", END, values=row)
            else:
                messagebox.showinfo(
                    "Failure!!", "No Record Found", parent=self.Department_win
                )
        except Exception as e:
            messagebox.showerror(
                "Query Error ",
                "Error in Query: \n" + str(e),
                parent=self.Department_win,
            )

    def updateDepartment(self):
        try:
            qry = (
                "update departments_table set Department_Head=%s where Department_Name=%s"
            )
            rowcount = self.current.execute(
                qry,
                (
                    self.DepartmentHeadEntry.get(),
                    self.DepartmentNameEntry.get()
                ),
            )
            self.connection.commit()
            if rowcount == 1:
                messagebox.showinfo(
                    "Success ", "Student Updated Successfully", parent=self.Department_win
                )
                self.Clear_all()

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Department_win
            )

    def DeleteDepartment(self):
        ans = messagebox.askquestion(
            "Confirmation", "Are you sure to delete ?", parent=self.Department_win
        )
        if ans == "yes":
            try:
                qry = "delete from departments_table where Department_Name=%s"
                rowcount = self.current.execute(qry, (self.DepartmentNameEntry.get()))
                self.connection.commit()
                if rowcount == 1:
                    messagebox.showinfo(
                        "Success ",
                        "Course deleted Successfully",
                        parent=self.Department_win,
                    )
                    self.Clear_all()

            except Exception as e:
                messagebox.showerror(
                    "Query Error ",
                    "Error in Query: \n" + str(e),
                    parent=self.Department_win,
                )

    def Clear_all(self):
        for entry in self.entry_list:
            entry.delete(0, END)

        self.Search_department()


if __name__ == "__main__":
    dummy_win = Tk()
    Departments_page(dummy_win)
