from settings import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox, Treeview
from PIL import Image, ImageTk
import pymysql


class Courses_page:
    def __init__(self, win):
        # ================== Defining Global variables ==================
        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================

        # ================== Creating window ==================
        self.Course_win = Toplevel(win)
        self.Course_win.state("zoomed")
        self.Course_win.config(background=bg_colour)
        # self.Course_win.wm_attributes('-transparentcolor', '#ab23ff')

        self.w = self.Course_win.winfo_screenwidth() - 700
        self.h = self.Course_win.winfo_screenheight() - 200

        # ================== Creating window ==================

        # ================== Setting up the window ==================
        self.Course_win.title("Courses")
        self.Course_win.geometry("%dx%d+%d+%d" % (self.w, self.h, 300, 50))
        self.W_w = self.Course_win.winfo_width()
        self.W_h = self.Course_win.winfo_height()

        # Background images =================
        self.image = Image.open("images//i4e2.jpg").resize([1920, 1080])

        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.Course_win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # Gtb logo imgage
        self.bgimage = Image.open("images//GTBlogo.jpg")

        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.Course_win, image=self.bgimage).place(
            x=1690, y=893
        )
        # Background images =================

        # self.Course_win.
        self.heading = Label(
            self.Course_win,
            text="COURSES",
            background=acent,
            foreground=bg_colour,
            font=heading_font,
            # relief="raised",
            borderwidth=15,
        )
        self.goback_btn = Button(
            self.Course_win,
            text="Bo Back",
            border=2,
            font=button_font,
            foreground=bg_colour,
            background=acent,
            command=lambda: self.Course_win.destroy(),
        )
        # ================== Setting up the window ==================

        # ================== Creating Frames ==================
        self.CourseInfo = Frame(
            self.Course_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=1000,
            height=240,
        )

        self.TableFrame = Frame(
            self.Course_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=1000,
            height=340,
        )
        # ================== Creating Frames ==================

        # =================== Course Frame elements ===================

        self.CourseFrameHeader = Label(
            self.CourseInfo,
            width=50,
            anchor="w",
            text="<<< Course Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        self.DepartmentVar = StringVar()
        self.DepartmentNameLabel = Label(
            self.CourseInfo,
            text="Department Name :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.DepartmentNameEntry = Combobox(
            self.CourseInfo,
            font=EntryFont,
            textvariable=self.DepartmentVar,
            width=26,
            state="readonly",
        )

        self.CourseNameLabel = Label(
            self.CourseInfo,
            text="Course Name :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.CourseNameEntry = Entry(
            self.CourseInfo,
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
        self.entry_list.append(self.CourseNameEntry)

        self.DurationLabel = Label(
            self.CourseInfo,
            text="Duration :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.DurationEntry = Entry(
            self.CourseInfo,
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
        self.entry_list.append(self.DurationEntry)

        self.FeeLabel = Label(
            self.CourseInfo,
            text="Fee :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.FeeEntry = Entry(
            self.CourseInfo,
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
        self.entry_list.append(self.FeeEntry)

        # Buttons ============================
        self.FetchCourse = Button(
            self.CourseInfo,
            text="Fetch (By Name)",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.fetchCourse,
        )
        self.SaveCourse = Button(
            self.CourseInfo,
            text="Save",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.AddCourse,
        )
        self.UpdateCourse = Button(
            self.CourseInfo,
            text="Update",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.updateCourse,
        )
        self.DeleteCourse = Button(
            self.CourseInfo,
            text="Delete",
            width=20,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.DeleteCourse,
        )

        # =================== Course Frame elements ===================

        # =================== Table Frame Elements ===================

        self.TableFrameHeader = Label(
            self.TableFrame,
            width=50,
            anchor="w",
            text="<<< Course Table >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        self.CourseTable = Treeview(
            self.TableFrame, columns=["c1", "c2", "c3", "c4"], height=11
        )
        self.CourseTable.heading("c1", text="Department")
        self.CourseTable.heading("c2", text="Course")
        self.CourseTable.heading("c3", text="Duration")
        self.CourseTable.heading("c4", text="Fee")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("#1", width=245, anchor=CENTER)
        self.CourseTable.column("#2", width=245, anchor=CENTER)
        self.CourseTable.column("#3", width=245, anchor=CENTER)
        self.CourseTable.column("#4", width=245, anchor=CENTER)

        self.CourseTable.bind("<ButtonRelease>", lambda e: self.GetPkVaue())

        self.SearchCourseNameLabel = Label(
            self.TableFrame,
            text="Course Name :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.SearchCourseNameEntry = Entry(
            self.TableFrame,
            width=57,
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
        self.SearchCourseNameEntry.bind("<KeyRelease>", lambda e: self.Search_course())
        self.SearchCourse = Button(
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
            command=self.Search_course,
        )

        # =================== Table Frame Elements ===================

        # =================== Placing ===================
        # main frame =================
        self.heading.pack(pady=10, fill=X)
        self.goback_btn.place(x=370, y=150)

        f_x = 30
        f_y = 60
        x_diff = 190
        y_diff = 60
        self.CourseFrameHeader.place(x=3, y=3)
        self.DepartmentNameLabel.place(x=f_x, y=f_y)
        self.DepartmentNameEntry.place(x=f_x + x_diff, y=f_y)
        self.DurationEntry.place(x=f_x + x_diff, y=f_y + y_diff)
        self.DurationLabel.place(x=f_x, y=f_y + y_diff)
        self.CourseNameLabel.place(x=90 + f_x + x_diff + x_diff, y=f_y)
        self.CourseNameEntry.place(x=90 + f_x + x_diff + x_diff + x_diff, y=f_y)
        self.FeeLabel.place(x=90 + f_x + x_diff + x_diff, y=f_y + y_diff)
        self.FeeEntry.place(x=90 + f_x + x_diff + x_diff + x_diff, y=f_y + y_diff)

        # buttons
        f_x = 35
        f_y = 60
        x_diff = 235
        y_diff = 60
        self.FetchCourse.place(x=f_x, y=f_y + y_diff + y_diff)
        self.SaveCourse.place(x=f_x + x_diff, y=f_y + y_diff + y_diff)
        self.UpdateCourse.place(x=f_x + x_diff + x_diff, y=f_y + y_diff + y_diff)
        self.DeleteCourse.place(
            x=f_x + x_diff + x_diff + x_diff, y=f_y + y_diff + y_diff
        )
        self.SearchCourse.place(x=f_x + x_diff + x_diff + x_diff, y=38)

        self.CourseInfo.pack()

        self.TableFrameHeader.place(x=3, y=3)
        self.SearchCourseNameLabel.place(x=10, y=40)
        self.SearchCourseNameEntry.place(x=180, y=40)
        self.CourseTable.place(x=10, y=80)
        self.TableFrame.pack(pady=10)
        # =================== Placing ===================

        self.DataBaseConnection()
        self.Clear_all()
        self.GetDepartments()
        self.Search_course()

        self.Course_win.mainloop()

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
                parent=self.Course_win,
            )

    def GetDepartments(self):
        try:
            query = "select * from departments_table"
            rowcount = self.current.execute(query)
            data = self.current.fetchall()
            self.departments_list = []
            if data:
                self.DepartmentNameEntry.set("Select Department")
                for row in data:
                    self.departments_list.append((row[0]))
            else:
                self.DepartmentNameEntry.set("No Department Available")

            self.DepartmentNameEntry.config(values=self.departments_list)

        except Exception as e:
            messagebox.showerror(
                "Query Error!!", "Error in Query:\n" + str(e), parent=self.Course_win
            )

    def AddCourse(self):
        Duration = self.DurationEntry.get() + " years"
        Fee = "Rs. " + self.FeeEntry.get()
        try:
            query = "insert into courses_table values(%s, %s, %s, %s)"
            rowcount = self.current.execute(
                query,
                (
                    self.DepartmentNameEntry.get(),
                    self.CourseNameEntry.get(),
                    Duration,
                    Fee,
                ),
            )
            self.connection.commit()

            if rowcount == 1:
                messagebox.showinfo(
                    "Success ", "Student Added Successfully", parent=self.Course_win
                )
                self.Clear_all()

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Course_win
            )

    def GetPkVaue(self):
        rowID = self.CourseTable.focus()

        data = self.CourseTable.item(rowID)

        StudentData = data["values"]

        pkValue = StudentData[1]

        self.fetchCourse(pkValue)

    def fetchCourse(self, pkValue=None):
        if pkValue == None:
            Course = self.CourseNameEntry.get()
        else:
            Course = pkValue
        try:
            query = "select * from courses_table where Course = %s"
            rowcount = self.current.execute(query, (Course))
            data = self.current.fetchone()
            self.Clear_all()
            if data:
                self.DepartmentNameEntry.set(data[0])
                self.CourseNameEntry.insert(0, data[1])
                self.DurationEntry.insert(0, data[2])
                self.FeeEntry.insert(0, data[3])

            else:
                messagebox.info(
                    "!!Failure!!", "No record Found", parent=self.Course.win
                )

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Course_win
            )

    def Search_course(self):
        try:
            query = "select * from courses_table where Course like %s"
            rewcount = self.current.execute(
                query, (self.SearchCourseNameEntry.get() + "%")
            )
            data = self.current.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            if data:
                for row in data:
                    self.CourseTable.insert("", END, values=row)
            else:
                messagebox.showinfo(
                    "Failure!!", "No Record Found", parent=self.Course_win
                )
        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Course_win
            )

    def updateCourse(self):
        try:
            query = "update courses_table set Department=%s, Duration=%s, Fee=%s where Course=%s"
            rowcount = self.current.execute(query, (
                self.DepartmentNameEntry.get(),
                self.DurationEntry.get(),
                self.FeeEntry.get(),
                self.CourseNameEntry.get()
            ))
            self.connection.commit()
            if rowcount==1:
                messagebox.showinfo("Success!!", "Course Updated Successfully", parent=self.Course_win)
                self.Clear_all()
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.Course_win)
            
    def DeleteCourse(self):
        ans = messagebox.askquestion(
            "Confirmation", "Are you sure to delete ?", parent=self.Course_win
        )
        if ans == "yes":
            try:
                qry = "delete from courses_table where Course=%s"
                rowcount = self.current.execute(qry, (self.CourseNameEntry.get()))
                self.connection.commit()
                if rowcount == 1:
                    messagebox.showinfo(
                        "Success ",
                        "Course deleted Successfully",
                        parent=self.Course_win,
                    )
                    self.Clear_all()

            except Exception as e:
                messagebox.showerror(
                    "Query Error ",
                    "Error in Query: \n" + str(e),
                    parent=self.Course_win,
                )

    def Clear_all(self):
        for entry in self.entry_list:
            entry.delete(0, END)
        self.DepartmentNameEntry.set("Select Value")

        self.Search_course()


if __name__ == "__main__":
    dummy_win = Tk()
    Courses_page(dummy_win)
