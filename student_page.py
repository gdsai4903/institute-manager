from settings import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import pymysql


class Student_page:
    default_image = "default.png"

    def __init__(self, win):
        # # ================== Defining Global variables ==================
        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================

        # ================== Creating window ==================
        self.Student_win = Toplevel(win)
        self.Student_win.state("zoomed")


        self.w = self.Student_win.winfo_screenwidth() - 700
        self.h = self.Student_win.winfo_screenheight() - 200

        # ================== Creating window ==================

        # ================== Setting up the window ==================
        self.Student_win.title("STUDENTS")
        self.Student_win.geometry("%dx%d+%d+%d" % (self.w, self.h, 300, 50))
        self.W_w = self.Student_win.winfo_width()
        self.W_h = self.Student_win.winfo_height()

        # # Background images =================
        self.image = Image.open("images//i4e2.jpg").resize([1920, 1080])
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.Student_win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # Gtb logo imgage
        self.bgimage = Image.open("images//GTBlogo.jpg")
        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.Student_win, image=self.bgimage)

        # Heading =================
        self.heading = Label(
            self.Student_win,
            text=" MANAGE STUDENTS ",
            background=acent,
            foreground=bg_colour,
            font=heading_font,
            # relief="raised",
            borderwidth=15,
        )

        # Go back Button ===============
        self.goback_btn = Button(
            self.Student_win,
            text="Bo Back",
            border=0,
            font=button_font,
            foreground=bg_colour,
            background=acent,
            command=lambda: self.Student_win.destroy(),
        )
        # ================== Setting up the window ==================

        # ================== Creating Frames ==================
        self.Personal_info = Frame(
            self.Student_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=1200,
            height=340,
        )

        self.c_s_frame = Frame(
            self.Student_win, width=1200, height=200, background="#6c7477"
        )
        self.Contact_info = Frame(
            self.c_s_frame,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=700 - 5,
            height=200,
        )
        self.Subject_info = Frame(
            self.c_s_frame,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=500 - 5,
            height=200,
        )
        self.Table_frame = Frame(
            self.Student_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=1200,
            height=300,
        )
        # ================== Creating Frames ==================

        # ================== Setting up personal frame ==================
        self.first_name_label = Label(
            self.Personal_info,
            text="First Name*",
            background=bg_colour,
            foreground="grey",
        )
        self.middle_name_label = Label(
            self.Personal_info,
            text="Middle Name",
            background=bg_colour,
            foreground="grey",
        )
        self.last_name_label = Label(
            self.Personal_info,
            text="Last Name",
            background=bg_colour,
            foreground="grey",
        )
        # ================== Setting up personal frame ==================

        # ================== Personal Info ==================
        # Frame Headers =================
        self.Personal_frame_header = Label(
            self.Personal_info,
            width=65,
            anchor="w",
            text="<<< Personal Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        # Rollno
        self.Rollno_label = Label(
            self.Personal_info,
            text="Roll No. *",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Rollno_entry = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            width=65,
            justify=CENTER,
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Rollno_entry)

        # Student Name
        self.Student_name_label = Label(
            self.Personal_info,
            text="Name*",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Student_first_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Student_first_name_in)
        self.Student_middle_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Student_middle_name_in)
        self.Student_last_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Student_last_name_in)

        # Father Name
        self.Father_name_label = Label(
            self.Personal_info,
            text="Father's Name",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Father_first_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Father_first_name_in)
        self.Father_middle_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Father_middle_name_in)
        self.Father_last_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Father_last_name_in)
        self.Father_name = (
            self.Father_first_name_in.get()
            + self.Father_middle_name_in.get()
            + self.Father_last_name_in.get()
        )

        # Mother Name
        self.Mother_name_label = Label(
            self.Personal_info,
            text="Mother's Name",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Mother_first_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Mother_first_name_in)
        self.Mother_middle_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Mother_middle_name_in)
        self.Mother_last_name_in = Entry(
            self.Personal_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        self.entry_list.append(self.Mother_last_name_in)

        # Address
        self.Address = Label(
            self.Personal_info,
            text="Address*",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.address_entry = Text(
            self.Personal_info,
            font=EntryFont,
            height=2,
            width=64,
            wrap="word",
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
        )
        # self.entry_list.append(self.address_entry)

        # Age
        self.Age = Label(
            self.Personal_info,
            text="D.O.B* (MM/DD/YY)",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Age_entry = DateEntry(
            self.Personal_info,
            font=font,
            date_pattern="dd-mm-y",
        )
        self.entry_list.append(self.Age_entry)

        # Gender
        self.Gender_var = StringVar()
        self.Gender_var.set(None)
        self.Gender = Label(
            self.Personal_info,
            text="Gender*",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Male_btn = Radiobutton(
            self.Personal_info,
            variable=self.Gender_var,
            text="Male",
            background=acent,
            foreground=bg_colour,
            value="male",
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
        )
        self.Female_btn = Radiobutton(
            self.Personal_info,
            variable=self.Gender_var,
            text="Female",
            background=acent,
            foreground=bg_colour,
            value="female",
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
        )

        # Default User Photo
        self.Student_img = Label(self.Personal_info,width=150, height=180)

        # Buttons
        self.add_image_btn = Button(
            self.Personal_info,
            text="Add Image",
            foreground=bg_colour,
            background=acent,
            width=14,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.AddImageForNewEntry,
        )
        self.fetch_btn = Button(
            self.Personal_info,
            text="Fetch",
            foreground=bg_colour,
            background=acent,
            width=13,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.fetchStudent,
        )
        self.Add_btn = Button(
            self.Personal_info,
            text="Save",
            foreground=bg_colour,
            background=acent,
            width=13,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.Add_Student,
        )
        self.Update_btn = Button(
            self.Personal_info,
            text="Update",
            foreground=bg_colour,
            background=acent,
            width=13,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.updateStudent,
        )
        self.Delete_btn = Button(
            self.Personal_info,
            text="Delete",
            foreground=bg_colour,
            background=acent,
            width=13,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.DeleteStudent,
        )
        self.Clear_btn = Button(
            self.Personal_info,
            text="Clear",
            foreground=bg_colour,
            background=acent,
            width=13,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            command=self.Clear_all,
            border=0,
        )
        # ================== Personal Info ==================

        # ================== Contact Info ==================

        # =================== Setting up Contact ===================
        self.Phone = Label(
            self.Contact_info,
            text="Phone*",
            background=bg_colour,
            foreground="grey",
        )
        self.Email = Label(
            self.Contact_info,
            text="Email Id",
            background=bg_colour,
            foreground="grey",
        )
        # =================== Setting up Contact ===================
        # Frame Headers =================
        self.Contact_frame_header = Label(
            self.Contact_info,
            width=38,
            anchor="w",
            text="<<<  Contact Details  >>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        # Phone
        self.Student_Phone = Label(
            self.Contact_info,
            text="Personal Contacts*",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Student_Phone_entry = Entry(
            self.Contact_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            width=25,
        )
        self.entry_list.append(self.Student_Phone_entry)
        self.Student_Email_entry = Entry(
            self.Contact_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            width=25,
        )
        self.entry_list.append(self.Student_Email_entry)

        # Father's Phone
        self.Father_Phone = Label(
            self.Contact_info,
            text="Father's Contacts",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Father_Phone_entry = Entry(
            self.Contact_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            width=25,
        )
        self.entry_list.append(self.Father_Phone_entry)
        self.Father_Email_entry = Entry(
            self.Contact_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            width=25,
        )
        self.entry_list.append(self.Father_Email_entry)

        # Mother's Phone
        self.Mother_Phone = Label(
            self.Contact_info,
            text="Mother's Contacts",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Mother_Phone_entry = Entry(
            self.Contact_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            width=25,
        )
        self.entry_list.append(self.Mother_Phone_entry)
        self.Mother_Email_entry = Entry(
            self.Contact_info,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            width=25,
        )
        self.entry_list.append(self.Mother_Email_entry)
        # ================== Contact Info ==================

        # =================== Subject Info ===================
        # Frame Headers =================
        self.Subject_frame_header = Label(
            self.Subject_info,
            width=24,
            anchor="w",
            text="<<<  Subject Details  >>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )
        # Department
        self.Department_var = StringVar()
        self.Department = Label(
            self.Subject_info,
            text="Department*",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Department_entry = Combobox(
            self.Subject_info,
            font=EntryFont,
            values=["hello"],
            state="readonly",
            textvariable=self.Department_var,
        )
        self.combobox_list.append(self.Department_entry)
        self.Department_entry.bind("<<ComboboxSelected>>", lambda e: self.GetCourses())

        # Course
        self.Course_var = StringVar()
        self.Course = Label(
            self.Subject_info,
            text="Course*",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Course_entry = Combobox(
            self.Subject_info,
            font=EntryFont,
            values=["world"],
            state="readonly",
            textvariable=self.Course_var,
        )
        self.combobox_list.append(self.Course_entry)

        # =================== Subject Info ===================

        # =================== Table Frame ===================
        # ------------ table ---------------------------
        self.Student_Table = Treeview(
            self.Table_frame,
            columns=["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"],
            height=11,
        )

        self.Student_Table.heading("c1", text="Roll no")
        self.Student_Table.heading("c2", text="Name")
        self.Student_Table.heading("c3", text="Father Name")
        self.Student_Table.heading("c4", text="Mother Name")
        self.Student_Table.heading("c5", text="DOB")
        self.Student_Table.heading("c6", text="Address")
        self.Student_Table.heading("c7", text="Gender")
        self.Student_Table.heading("c8", text="Phone")
        self.Student_Table.heading("c9", text="E-mail")

        self.Student_Table["show"] = "headings"
        self.Student_Table.column("#1", width=80, anchor="center")
        self.Student_Table.column("#2", width=140, anchor="center")
        self.Student_Table.column("#3", width=140, anchor="center")
        self.Student_Table.column("#4", width=140, anchor="center")
        self.Student_Table.column("#5", width=100, anchor="center")
        self.Student_Table.column("#6", width=200, anchor="center")
        self.Student_Table.column("#7", width=100, anchor="center")
        self.Student_Table.column("#8", width=100, anchor="center")
        self.Student_Table.column("#9", width=180, anchor="center")

        self.Search_name_in_table = Label(
            self.Table_frame,
            text="Name: ",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.Search_name_in_table_entry = Entry(
            self.Table_frame,
            font=EntryFont,
            background=bg_colour,
            foreground="white",
            border=entry_border_thickness,
            relief=entry_releif,
            highlightcolor=fg_colour,
            highlightbackground=entry_highlight_bg_colour,
            highlightthickness=entry_border_highlight_thickness,
            insertbackground=fg_colour,
            width=65,
        )
        
        # self.Search_name_in_table_entry.bind("<KeyRelease>", lambda x: self.Search_student())
        self.Search_btn = Button(
            self.Table_frame,
            text="Search",
            foreground=bg_colour,
            background=acent,
            width=13,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            command=self.Search_student,
            border=0,
        )

        self.Student_Table.bind("<ButtonRelease>", lambda e: self.GetPkVaue())
        # =================== Table Frame ===================

        # ================== Placments ==================
        # Placing the personal frame
        self.heading.pack(pady=10, fill=X)
        self.goback_btn.place(x=270, y=150)
        self.gtb_logo_img.place(x=1690, y=893)
        self.Personal_info.pack()
        self.Personal_frame_header.place(x=3, y=3)

        self.Contact_info.place(x=0, y=0)
        self.Contact_frame_header.place(x=3, y=3)

        self.Subject_info.place(x=705, y=0)
        self.Subject_frame_header.place(x=3, y=3)

        self.c_s_frame.pack(pady=10)

        self.Search_name_in_table.place(x=7, y=7)
        self.Search_name_in_table_entry.place(x=90, y=11)
        self.Search_btn.place(x=700, y=7)
        self.Student_Table.place(x=7, y=45)
        self.Table_frame.pack()

        f_x = 10
        f_y = 80
        x_diff = 200
        y_diff = 40
        self.first_name_label.place(x=75 + x_diff, y=f_y + 5)
        self.middle_name_label.place(x=65 + x_diff + x_diff, y=f_y + 5)
        self.last_name_label.place(x=70 + x_diff + x_diff + x_diff, y=f_y + 5)
        self.Student_img.place(x=35 + x_diff + x_diff + x_diff + x_diff, y=f_y + 5)

        f_x += 0
        self.Rollno_label.place(x=f_x, y=f_y - 30)
        self.Rollno_entry.place(x=f_x + x_diff, y=f_y - 30)
        f_y += y_diff - 10
        self.Student_name_label.place(x=f_x, y=f_y)
        self.Student_first_name_in.place(x=f_x + x_diff, y=f_y)
        self.Student_middle_name_in.place(x=f_x + x_diff + x_diff, y=f_y)
        self.Student_last_name_in.place(x=f_x + x_diff + x_diff + x_diff, y=f_y)

        f_x += 0
        f_y += y_diff
        self.Father_name_label.place(x=f_x, y=f_y)
        self.Father_first_name_in.place(x=f_x + x_diff, y=f_y)
        self.Father_middle_name_in.place(x=f_x + x_diff + x_diff, y=f_y)
        self.Father_last_name_in.place(x=f_x + x_diff + x_diff + x_diff, y=f_y)

        f_x += 0
        f_y += y_diff
        self.Mother_name_label.place(x=f_x, y=f_y)
        self.Mother_first_name_in.place(x=f_x + x_diff, y=f_y)
        self.Mother_middle_name_in.place(x=f_x + x_diff + x_diff, y=f_y)
        self.Mother_last_name_in.place(x=f_x + x_diff + x_diff + x_diff, y=f_y)

        f_x += 0
        f_y += y_diff
        self.Address.place(x=f_x, y=f_y)
        self.address_entry.place(x=f_x + x_diff, y=f_y)

        f_x += 0
        f_y += y_diff + 20
        self.Age.place(x=f_x, y=f_y)
        self.Age_entry.place(x=f_x + x_diff, y=f_y)

        self.Gender.place(x=f_x + x_diff + x_diff, y=f_y)
        self.Male_btn.place(x=f_x + x_diff + x_diff + 100, y=f_y)
        self.Female_btn.place(x=f_x + x_diff + x_diff + 200, y=f_y)

        self.add_image_btn.place(x=38 + x_diff + x_diff + x_diff + x_diff, y=f_y - 7)

        f_y = 70
        y_diff = 50
        self.fetch_btn.place(x=30 + x_diff + x_diff + x_diff + x_diff + x_diff, y=f_y)
        self.Clear_btn.place(
            x=30 + x_diff + x_diff + x_diff + x_diff + x_diff, y=f_y + y_diff
        )
        self.Add_btn.place(
            x=30 + x_diff + x_diff + x_diff + x_diff + x_diff,
            y=f_y + y_diff + y_diff,
        )
        self.Update_btn.place(
            x=30 + x_diff + x_diff + x_diff + x_diff + x_diff,
            y=f_y + y_diff + y_diff + y_diff,
        )
        self.Delete_btn.place(
            x=30 + x_diff + x_diff + x_diff + x_diff + x_diff,
            y=f_y + y_diff + y_diff + y_diff + y_diff,
        )

        # Placing the personal frame

        # Placing the Contact frame
        f_x = 10
        f_y = 50
        x_diff = 220
        y_diff = 40

        f_x += 235
        self.Phone.place(x=f_x, y=f_y)
        self.Email.place(x=f_x + 200, y=f_y)

        f_x = 10
        f_y += y_diff - 15
        self.Student_Phone.place(x=f_x, y=f_y)
        self.Father_Phone.place(x=f_x, y=f_y + y_diff)
        self.Mother_Phone.place(x=f_x, y=f_y + y_diff + y_diff)
        self.Student_Phone_entry.place(x=f_x + x_diff - 20, y=f_y)
        self.Father_Phone_entry.place(x=f_x + x_diff - 20, y=f_y + y_diff)
        self.Mother_Phone_entry.place(x=f_x + x_diff - 20, y=f_y + y_diff + y_diff)
        self.Student_Email_entry.place(x=f_x + x_diff + x_diff, y=f_y)
        self.Father_Email_entry.place(x=f_x + x_diff + x_diff, y=f_y + y_diff)
        self.Mother_Email_entry.place(x=f_x + x_diff + x_diff, y=f_y + y_diff + y_diff)
        # Placing the Contact frame

        # Placing the Subject frame
        f_x = 10
        f_y = 70
        x_diff = 120
        y_diff = 40

        f_x += 0
        self.Department.place(x=f_x, y=f_y)
        self.Department_entry.place(x=f_x + x_diff, y=f_y)

        f_x += 0
        f_y += y_diff
        self.Course.place(x=f_x, y=f_y)
        self.Course_entry.place(x=f_x + x_diff, y=f_y)
        # Placing the Subject frame
        # ================== Placments ==================

        # =================== Database Functions ===================
        self.DataBaseConnection()
        self.Clear_all()
        self.GetDepartments()
        self.Search_student()
        # =================== Database Functions ===================

        self.Student_win.mainloop()

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

    def AddImageForNewEntry(self):
        self.filename = askopenfilename(
            parent=self.Student_win,
            file=[
                ("All Pictures", "*.png;*.jpg;*.jpeg"),
                ("PNG Images", "*.png"),
                ("JPG Images", "*.jpg"),
            ],
        )

        if self.filename != "":
            self.temp_img1 = Image.open(self.filename).resize((150, 180))
            self.temp_img2 = ImageTk.PhotoImage(self.temp_img1)
            self.Student_img.config(image=self.temp_img2, border=0)

            image_path = self.filename.split("/")  # getting the path to the image
            image_name = image_path[-1]  # getting name of the image

            import time

            uniqness = str(int(time.time()))  # getting a unique ID for each image
            self.Student_image_name = (
                uniqness + image_name
            )  # creating a unique name for each image.strip()

    def Search_student(self):
        try:
            query = "select * from students_table where S_Name like %s"
            rewcount = self.current.execute(
                query, (self.Search_name_in_table_entry.get() + "%")
            )
            data = self.current.fetchall()
            self.Student_Table.delete(*self.Student_Table.get_children())
            if data:
                for row in data:
                    self.Student_Table.insert("", END, values=row)
                error_shown = 0
            else:
                if error_shown == 0:
                    messagebox.showinfo(
                        "Failure!!", "No Record Found", parent=self.Student_win
                    )
                    error_shown = 1
        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Student_win
            )

    def Add_Student(self):
        if self.checkValidation() == False:
            return
        self.Student_name = self.CombineName(self.Student_first_name_in.get().strip(), self.Student_middle_name_in.get().strip() , self.Student_last_name_in.get().strip())
        
        self.Father_name = self.CombineName(self.Father_first_name_in.get().strip(), self.Father_middle_name_in.get().strip() , self.Father_last_name_in.get().strip())
        
        self.Mother_name = self.CombineName(self.Mother_first_name_in.get().strip(), self.Mother_middle_name_in.get().strip() , self.Mother_last_name_in.get().strip())

        if self.Student_image_name == self.default_image:  # no new img is selected
            # nothing to save in folder
            pass
        else:  # image is selected
            self.temp_img1.save("images//Student_images//" + self.Student_image_name)

        try:
            query = "insert into students_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.current.execute(
                query,
                (
                    self.Rollno_entry.get(),
                    self.Student_name,
                    self.Father_name,
                    self.Mother_name,
                    self.Age_entry.get_date(),
                    self.address_entry.get("1.0", END),
                    self.Gender_var.get(),
                    self.Student_Phone_entry.get(),
                    self.Student_Email_entry.get(),
                    self.Father_Phone_entry.get(),
                    self.Father_Email_entry.get(),
                    self.Mother_Phone_entry.get(),
                    self.Mother_Email_entry.get(),
                    self.Department_var.get(),
                    self.Course_var.get(),
                    self.Student_image_name,
                ),
            )
            self.connection.commit()

            if rowcount == 1:
                messagebox.showinfo(
                    "Success ", "Student Added Successfully", parent=self.Student_win
                )
                self.Clear_all()

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Student_win
            )

    def GetPkVaue(self):
        rowID = self.Student_Table.focus()

        data = self.Student_Table.item(rowID)

        StudentData = data["values"]

        pkValue = StudentData[0]

        self.fetchStudent(pkValue)

    def fetchStudent(self, pkValue=None):
        if pkValue == None:
            rollno = self.Rollno_entry.get()
        else:
            rollno = pkValue
        try:
            query = "select * from students_table where RollNo = %s"
            rowcount = self.current.execute(query, (rollno))
            data = self.current.fetchone()
            self.Clear_all()
            if data:
                self.Rollno_entry.insert(0, data[0])
                
                student_f, student_m, student_l = self.SplitName(data[1])
                self.Student_first_name_in.insert(0, student_f)
                self.Student_middle_name_in.insert(0, student_m)
                self.Student_last_name_in.insert(0, student_l)
                
                
                Father_f, Father_m, Father_l = self.SplitName(data[2])
                self.Father_first_name_in.insert(0, Father_f)
                self.Father_middle_name_in.insert(0, Father_m)
                self.Father_last_name_in.insert(0, Father_l)
                
                Mother_f, Mother_m, Mother_l = self.SplitName(data[3])
                self.Mother_first_name_in.insert(0, Mother_f)
                self.Mother_middle_name_in.insert(0, Mother_m)
                self.Mother_last_name_in.insert(0, Mother_l)
                
                self.Age_entry.set_date(data[4])
                self.address_entry.insert("1.0", data[5])
                self.Gender_var.set(data[6])
                self.Student_Phone_entry.insert(0, data[7])
                self.Student_Email_entry.insert(0, data[8])
                self.Father_Phone_entry.insert(0, data[9])
                self.Father_Email_entry.insert(0, data[10])
                self.Mother_Phone_entry.insert(0, data[11])
                self.Mother_Email_entry.insert(0, data[12])
                self.Department_entry.set(data[13])
                self.Course_entry.set(data[14])
                
                self.Student_image_name = data[15]
                self.Previous_img_name = data[15]

                # print(self.Previous_img_name)
                self.temp_img1 = Image.open(
                    "images//Student_images//" + self.Previous_img_name
                ).resize((150, 180))
                # print(self.temp_img1)
                self.temp_img2 = ImageTk.PhotoImage(self.temp_img1)
                self.Student_img.config(image=self.temp_img2)
                # print(self.Previous_img_name)
                # print(self.Student_image_name)

            else:
                messagebox.info(
                    "!!Failure!!", "No record Found", parent=self.Student_win
                )

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Student_win
            )

    def GetDepartments(self):
        try:
            query = "select * from departments_table"
            rowcount = self.current.execute(query)
            data = self.current.fetchall()
            self.departments_list = []
            if data:
                self.Department_entry.set("Select Department")
                for row in data:
                    self.departments_list.append((row[0]))
            else:
                self.Department_entry.set("No Department Available")

            self.Department_entry.config(values=self.departments_list)

        except Exception as e:
            messagebox.showerror(
                "Query Error!!", "Error in Query:\n" + str(e), parent=self.Student_win
            )

    def GetCourses(self):
        try:
            query = "select * from courses_table where Department = %s"
            rowcount = self.current.execute(query, (self.Department_entry.get()))
            data = self.current.fetchall()
            self.course_list = []
            if data:
                self.Course_entry.set("Select Course")
                for row in data:
                    self.course_list.append(row[1])
            else:
                self.Course_entry.set("No Course Available")

            self.Course_entry.config(values=self.course_list)
        except Exception as e:
            messagebox.showerror(
                "Querry Error!!", "Error in Query: \n" + str(e), parent=self.Student_win
            )

    def updateStudent(self):
        if self.checkValidation() == False:
            return  # end function now

        if self.Student_image_name == self.Previous_img_name:  # no new image is selected
            # nothing to save or delete in folder
            pass
        else:
            self.temp_img1.save("images//Student_images//" + self.Student_image_name)
            if self.Previous_img_name == self.default_image:  # no image was given in past
                # nothing to delete
                pass
            else:
                import os

                os.remove("images//Student_images//" + self.Previous_img_name)
        
        self.Student_name = self.CombineName(self.Student_first_name_in.get().strip(), self.Student_middle_name_in.get().strip() , self.Student_last_name_in.get().strip())
        
        self.Father_name = self.CombineName(self.Father_first_name_in.get().strip(), self.Father_middle_name_in.get().strip() , self.Father_last_name_in.get().strip())
        
        self.Mother_name = self.CombineName(self.Mother_first_name_in.get().strip(), self.Mother_middle_name_in.get().strip() , self.Mother_last_name_in.get().strip())

        try:
            qry = (
                "update students_table set S_name=%s, F_name=%s, M_name=%s, DOB=%s, Address=%s, Gender=%s, S_Phone=%s, S_email=%s, F_Phone=%s, F_email=%s, M_Phone=%s, M_email=%s, Department=%s, Course=%s, S_img=%s where RollNo=%s"
            )
            rowcount = self.current.execute(
                qry,
                (
                    self.Student_name,
                    self.Father_name,
                    self.Mother_name,
                    
                    self.Age_entry.get_date(),
                    self.address_entry.get("1.0", END),
                    self.Gender_var.get(),
                    
                    self.Student_Phone_entry.get(),
                    self.Student_Email_entry.get(),
                    
                    self.Father_Phone_entry.get(),
                    self.Father_Email_entry.get(),
                    
                    self.Mother_Phone_entry.get(),
                    self.Mother_Email_entry.get(),
                    
                    self.Department_entry.get(),
                    self.Course_entry.get(),
                    self.Student_image_name,
                    self.Rollno_entry.get(),
                ),
            )
            self.connection.commit()
            if rowcount == 1:
                messagebox.showinfo(
                    "Success ", "Student Updated Successfully", parent=self.Student_win
                )
                self.Clear_all()

        except Exception as e:
            messagebox.showerror(
                "Query Error ", "Error in Query: \n" + str(e), parent=self.Student_win
            )

    def DeleteStudent(self):
        ans = messagebox.askquestion(
            "Confirmation", "Are you sure to delete ?", parent=self.Student_win
        )
        if ans == "yes":

            if self.Previous_img_name == self.default_image:  # no image was given in past
                # nothing to delete
                pass
            else:
                import os

                os.remove("images//Student_images//" + self.Previous_img_name)
            try:
                qry = "delete from students_table where rollno=%s"
                rowcount = self.current.execute(qry, (self.Rollno_entry.get()))
                self.connection.commit()
                if rowcount == 1:
                    messagebox.showinfo(
                        "Success ",
                        "Student deleted Successfully",
                        parent=self.Student_win,
                    )
                    self.Clear_all()

            except Exception as e:
                messagebox.showerror(
                    "Query Error ",
                    "Error in Query: \n" + str(e),
                    parent=self.Student_win,
                )

    def checkValidation(self):
        if len(self.Rollno_entry.get()) < 1 or not self.Rollno_entry.get().isdigit():
            messagebox.showwarning(
                "Validation Check", "Enter Proper Roll no ", parent=self.Student_win
            )
            return False
        elif len(self.Student_first_name_in.get()) < 1:
            messagebox.showwarning(
                "Validation Check", "Student's First Name is necessary!", parent=self.Student_win
            )
            return False
        elif (
            len(self.Student_Phone_entry.get()) < 7
            or len(self.Student_Phone_entry.get()) > 15
            or not self.Student_Phone_entry.get().isdigit()
        ):
            messagebox.showwarning(
                "Validation Check",
                "Enter Proper (Student) Phone no\n[7-15 digits] ",
                parent=self.Student_win,
            )
            return False
        elif not (self.Gender_var.get() == "male" or self.Gender_var.get() == "female"):
            messagebox.showwarning(
                "Validation Check", "Select Gender ", parent=self.Student_win
            )
            return False
        elif self.Age_entry.get() == "":
            messagebox.showwarning(
                "Validation Check", "Select DOB ", parent=self.Student_win
            )
            return False
        elif len(self.address_entry.get("1.0", END)) < 2:
            messagebox.showwarning(
                "Validation Check", "Enter Address ", parent=self.Student_win
            )
            return False
        elif self.Department_entry.get() == "Select Department" or self.Department_entry.get() == "No Department":
            messagebox.showwarning(
                "Validation Check", "Select Department ", parent=self.Student_win
            )
            return False
        elif self.Course_entry.get() == "Select Course" or self.Course_entry.get() == "No Course":
            messagebox.showwarning(
                "Validation Check", "Select Course ", parent=self.Student_win
            )
            return False
        return True

    def CombineName(self, f, m, l):
        return f + " " + m + " " + l

    def SplitName(self, fullName):
        f, m, l = fullName.split(" ")
        return f, m, l
      
    def Clear_all(self):
        self.address_entry.delete("1.0", "end")
        for entry in self.entry_list:
            entry.delete(0, END)

        self.Course_entry.set("Select Course")
        self.Department_entry.set("Select Department")

        self.Student_image_name = self.default_image
        self.temp_img1 = Image.open("images//student_images//"+self.default_image).resize([150, 180])
        self.temp_img2 = ImageTk.PhotoImage(self.temp_img1)
        self.Student_img.config(image=self.temp_img2)

        self.Search_student()
  

if __name__ == "__main__":
    dummy_win = Tk()
    Student_page(dummy_win)
