from settings import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from PDF_Page import *
import pymysql
from PIL import Image, ImageTk


class Report_page:
    def __init__(self,win):
        # ================== Defining Global variables ==================
        self.entry_list = []
        self.combobox_list = []
        self.filters_for_students = ["all", "male", "female"]
        self.filters_for_departments = ["all"]
        self.filters_for_courses = ["all"]
        # =================== Defining Global variables ===================

        # =================== Creating main window ===================
        self.win = Toplevel(win)
        self.w = self.win.winfo_screenwidth() - 700
        self.h = self.win.winfo_screenheight() - 150
        # =================== Creating main window ===================

        # =================== Setting up the window ===================
        self.win.title("STUDENTS MANAGER")
        self.win.geometry("%dx%d+%d+%d" % (self.w, self.h, 350, 25))
        self.win.state("zoomed")
        self.win.option_add("*TearOff", False)
        self.menu_bar = Menu(self.win)
        self.win.config(menu=self.menu_bar, background=acent)

        # Background Image
        self.image = Image.open(
            "./images//i4e2.jpg"
        ).resize([1920, 1080])
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # =================== Setting up the window ===================

        # =================== Creating Frames ===================
        self.main_frame = Frame(
            self.win,
            background=bg_colour,
            width=1700,
            height=880,
            relief=frame_releif,
            border=frame_border_thickness,
        )
        # =================== Creating Frames ===================

        # =================== Labels ===================
        
        # Go back Button ===============
        self.goback_btn = Button(
            self.win,
            text="Bo Back",
            border=0,
            font=button_font,
            foreground=bg_colour,
            background=acent,
            command=lambda: self.win.destroy(),
        )

        self.Heading = Label(
            self.win,
            text="REPORTS",
            background=bg_colour,
            foreground=fg_colour,
            font=heading_font,
        )
        
        self.ReportHeader = Label(
            self.main_frame,
            width=90,
            anchor="w",
            text="<<<  All Reports  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )
        
        self.ReportTable = Treeview(self.main_frame, columns=["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15"], height=36)
        
        self.ReportTable.heading("c1", text="Roll No:")
        self.ReportTable.heading("c2", text="Student Name:")
        self.ReportTable.heading("c3", text="Father Name:")
        self.ReportTable.heading("c4", text="Mother Name:")
        self.ReportTable.heading("c5", text="DOB :")
        self.ReportTable.heading("c6", text="Address :")
        self.ReportTable.heading("c7", text="Gender:")
        self.ReportTable.heading("c8", text="Student Phone:")
        self.ReportTable.heading("c9", text="Student Email:")
        self.ReportTable.heading("c10", text="Father Phone:")
        self.ReportTable.heading("c11", text="Father Email:")
        self.ReportTable.heading("c12", text="Mother Phone:")
        self.ReportTable.heading("c13", text="Mother Email:")
        self.ReportTable.heading("c14", text="Department:")
        self.ReportTable.heading("c15", text="Course:")
        
        self.ReportTable["show"] = "headings"
        
        
        self.ReportTable.column("#1", width=100, anchor="center")
        self.ReportTable.column("#2", width=120, anchor="center")
        self.ReportTable.column("#3", width=120, anchor="center")
        self.ReportTable.column("#4", width=120, anchor="center")
        self.ReportTable.column("#5", width=70, anchor="center")
        self.ReportTable.column("#6", width=200, anchor="center")
        self.ReportTable.column("#7", width=85, anchor="center")
        self.ReportTable.column("#8", width=100, anchor="center")
        self.ReportTable.column("#9", width=120, anchor="center")
        self.ReportTable.column("#10", width=100, anchor="center")
        self.ReportTable.column("#11", width=120, anchor="center")
        self.ReportTable.column("#12", width=100, anchor="center")
        self.ReportTable.column("#13", width=120, anchor="center")
        self.ReportTable.column("#14", width=100, anchor="center")
        self.ReportTable.column("#15", width=100, anchor="center")



        self.CategoryVar = StringVar()
        self.CategoryLabel = Label(
            self.main_frame,
            text="Category : ",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.CategoryOption = Combobox(
            self.main_frame,
            font=EntryFont,
            values=["Students", "Department", "Course"],
            state="readonly",
            textvariable=self.CategoryVar,
        )
        self.CategoryOption.bind("<<ComboboxSelected>>", lambda x : self.changeFilters())
        
        self.FilterVar = StringVar()
        self.FilterLabel = Label(
            self.main_frame,
            text="Filter : ",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.FilterOption = Combobox(
            self.main_frame,
            font=EntryFont,
            state="readonly",
            textvariable=self.FilterVar,
        )
        self.FilterOption.bind("<<ComboboxSelected>>", lambda x : self.Search_student())

        self.Print_btn = Button(
            self.main_frame,
            text="Print",
            foreground=bg_colour,
            background=acent,
            width=13,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.Print,
        )

        # =================== Labels ===================

        # =================== Placing ===================
        self.Heading.pack(pady=10, fill=X)
        self.main_frame.pack()
        self.goback_btn.place(x=20, y=130)
        
        x = 10
        y = 60
        xd = 120
        yd = 40
        self.ReportHeader.place(x=3, y=3)
        self.CategoryLabel.place(x=x, y=y)
        self.CategoryOption.place(x=x+xd, y=y)
        self.FilterLabel.place(x=x+xd+xd+xd+xd, y=y)
        self.FilterOption.place(x=x+xd+xd+xd+xd+xd, y=y)
        self.Print_btn.place(x=x+xd+xd+xd+xd+xd+xd+xd+xd+xd+xd+xd, y=y-2)
        self.ReportTable.place(x=10, y=110)
        # =================== Placing ===================
        
        self.DataBaseConnection()
        self.Clear_all()
        self.GetDepartments()
        self.GetCourses()
        self.Search_student()
        self.win.mainloop()


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
                parent=self.Student_win,
            )

    def Search_student(self):
        self.PrintData = []
        if self.CategoryVar.get() == "select value":
            query = "select * from students_table where S_Name like %s"
            try:
                rewcount = self.current.execute(
                    query, ("%")
                )
                data = self.current.fetchall()
                self.ReportTable.delete(*self.ReportTable.get_children())
                if data:
                    for row in data:
                        self.PrintData.append(row[:-1])
                        self.ReportTable.insert("", END, values=row)
                else:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.win
                    )
            except Exception as e:
                messagebox.showerror(
                    "Query Error ", "Error in Query: \n" + str(e), parent=self.win
                )
                
        if self.CategoryVar.get() == "Students" and self.FilterVar.get() == "all":
            query = "select * from students_table where S_Name like %s"
            try:
                rewcount = self.current.execute(
                    query, ("%")
                )
                data = self.current.fetchall()
                self.ReportTable.delete(*self.ReportTable.get_children())
                if data:
                    for row in data:
                        self.PrintData.append(row[:-1])
                        self.ReportTable.insert("", END, values=row)
                else:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.win
                    )
            except Exception as e:
                messagebox.showerror(
                    "Query Error ", "Error in Query: \n" + str(e), parent=self.win
                )
                
        if self.CategoryVar.get() == "Students" and (self.FilterVar.get() == "male" or self.FilterVar.get() == "female"):
            query = "select * from students_table where Gender like %s"
            try:
                rewcount = self.current.execute(
                    query, (self.FilterVar.get())
                )
                data = self.current.fetchall()
                self.ReportTable.delete(*self.ReportTable.get_children())
                if data:
                    for row in data:
                        self.PrintData.append(row[:-1])
                        self.ReportTable.insert("", END, values=row)
                else:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.win
                    )
            except Exception as e:
                messagebox.showerror(
                    "Query Error ", "Error in Query: \n" + str(e), parent=self.win
                )

        if self.CategoryVar.get() == "Department" and self.FilterVar.get() == "all":
            query = "select * from students_table where Department like %s"
            try:
                rewcount = self.current.execute(
                    query, ("%")
                )
                data = self.current.fetchall()
                self.ReportTable.delete(*self.ReportTable.get_children())
                if data:
                    for row in data:
                        self.PrintData.append(row[:-1])
                        self.ReportTable.insert("", END, values=row)
                else:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.win
                    )
            except Exception as e:
                messagebox.showerror(
                    "Query Error ", "Error in Query: \n" + str(e), parent=self.win
                )
                
        if self.CategoryVar.get() == "Department" and (self.FilterVar.get() != "all"):
            query = "select * from students_table where Department like %s"
            try:
                rewcount = self.current.execute(
                    query, (self.FilterVar.get())
                )
                data = self.current.fetchall()
                self.ReportTable.delete(*self.ReportTable.get_children())
                if data:
                    for row in data:
                        self.PrintData.append(row[:-1])
                        self.ReportTable.insert("", END, values=row)
                else:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.win
                    )
            except Exception as e:
                messagebox.showerror(
                    "Query Error ", "Error in Query: \n" + str(e), parent=self.win
                )

        if self.CategoryVar.get() == "Course" and self.FilterVar.get() == "all":
            query = "select * from students_table where Department like %s"
            try:
                rewcount = self.current.execute(
                    query, ("%")
                )
                data = self.current.fetchall()
                self.ReportTable.delete(*self.ReportTable.get_children())
                if data:
                    for row in data:
                        self.PrintData.append(row[:-1])
                        self.ReportTable.insert("", END, values=row)
                else:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.win
                    )
            except Exception as e:
                messagebox.showerror(
                    "Query Error ", "Error in Query: \n" + str(e), parent=self.win
                )
                
        if self.CategoryVar.get() == "Course" and (self.FilterVar.get() != "all"):
            query = "select * from students_table where Course like %s"
            try:
                rewcount = self.current.execute(
                    query, (self.FilterVar.get())
                )
                data = self.current.fetchall()
                self.ReportTable.delete(*self.ReportTable.get_children())
                if data:
                    for row in data:
                        self.PrintData.append(row[:-1])
                        self.ReportTable.insert("", END, values=row)
                else:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.win
                    )
            except Exception as e:
                messagebox.showerror(
                    "Query Error ", "Error in Query: \n" + str(e), parent=self.win
                )

    def changeFilters(self):
        if self.CategoryVar.get() == "Students":
            self.FilterOption.config(values=self.filters_for_students)
        elif self.CategoryVar.get() == "Department":
            self.FilterOption.config(values=self.filters_for_departments)
        elif self.CategoryVar.get() == "Course":
            self.FilterOption.config(values=self.filters_for_courses)

    def GetDepartments(self):
        try:
            query = "select * from departments_table"
            rowcount = self.current.execute(query)
            data = self.current.fetchall()
            if data:
                for row in data:
                    self.filters_for_departments.append((row[0]))
            else:
                self.filters_for_departments=["No Departments available"]

        except Exception as e:
            messagebox.showerror(
                "Query Error!!", "Error in Query:\n" + str(e), parent=self.Course_win
            )

    def GetCourses(self):
        try:
            query = "select * from courses_table"
            rowcount = self.current.execute(query)
            data = self.current.fetchall()
            if data:
                for row in data:
                    self.filters_for_courses.append((row[1]))
            else:
                self.filters_for_courses=["No Departments available"]

        except Exception as e:
            messagebox.showerror(
                "Query Error!!", "Error in Query:\n" + str(e), parent=self.Course_win
            )

    def Print(self):
        print = PDF_page('L', "mm", (200, 600))
        headings = ["Roll No.", "S_Name", "F_Name", "M_Name", "DOB", "Address",
                    "Gender", "S_Phone", "S_Email", "F_Phone", "F_Email",
                    "M_Phone", "M_Email", "Department", "Course"]
        print.print_chapter(self.PrintData, headings, 15)
        print.output(f"pdf_file{self.FilterVar.get()}.pdf")
        os.system(f'explorer.exe "pdf_file{self.FilterVar.get()}.pdf"')
         
    def Clear_all(self):
        self.CategoryOption.set("select value")
        self.FilterOption.set("select value")

        
if __name__ == "__main__":
    dummy =Tk()
    Report_page(dummy)
