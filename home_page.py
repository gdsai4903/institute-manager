from settings import *
from tkinter import *
from tkinter.ttk import Combobox
from student_page import *
from departments_page import *
from courses_page import *
from users_page import *
from change_password_page import *
from reports_page import *
from PIL import Image, ImageTk


class Homepage:
    def __init__(self, UserName, UserType):
        # ================== Defining Global variables ==================
        self.utype = UserType
        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================

        # =================== Creating main window ===================
        self.win = Tk()
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

        # Gtb logo imgage
        self.bgimage = Image.open(
            "./images//GTBlogo.jpg"
        )
        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.win, image=self.bgimage).place(x=1690, y=875)
        # =================== Setting up the window ===================

        # =================== Creating Menus ===================
        self.manage_menu = Menu(self.menu_bar)
        self.department_menu = Menu(self.menu_bar)
        self.account_menu = Menu(self.menu_bar)
        self.Report_menu = Menu(self.menu_bar)
        # =================== Creating Menus ===================

        # =================== Adding options to the Menubar ===================
        # manage Menu
        self.menu_bar.add_cascade(menu=self.manage_menu, label="Manage")
        self.icon = Image.open("images//icons//students.png").resize((20, 20))
        self.st_icon = ImageTk.PhotoImage(self.icon)
        self.manage_menu.add_command(
            label="Student",
            command=lambda: Student_page(self.win),
            accelerator="Ctrl+Shift+S",
            image=self.st_icon,
            compound=LEFT,
        )
        self.win.bind("<Control-Shift-S>", lambda x: Student_page(self.win))

        # Department Menu
        self.menu_bar.add_cascade(menu=self.department_menu, label="Departments")
        self.icon = Image.open("images//icons//department.png").resize((20, 20))
        self.depart_icon = ImageTk.PhotoImage(self.icon)
        self.department_menu.add_command(
            label="Departments",
            command=lambda: Departments_page(self.win),
            accelerator="Ctrl+Shift+D",
            image=self.depart_icon,
            compound=LEFT,
        )
        self.win.bind("<Control-Shift-D>", lambda x: Departments_page(self.win))
        self.icon = Image.open("images//icons//online-course.png").resize((20, 20))
        self.course_icon = ImageTk.PhotoImage(self.icon)
        self.department_menu.add_command(
            label="Courses",
            command=lambda: Courses_page(self.win),
            accelerator="Ctrl+Shift+C",
            image=self.course_icon,
            compound=LEFT,
        )
        self.win.bind("<Control-Shift-C>", lambda x: Courses_page(self.win))

        # Report Menu
        self.icon = Image.open("images//icons//report.png").resize((20, 20))
        self.report_icon = ImageTk.PhotoImage(self.icon)
        self.menu_bar.add_cascade(menu=self.Report_menu, label="Reports")
        self.Report_menu.add_command(
            label="All Reports",
            command=lambda: Report_page(self.win),
            accelerator="Ctrl+Shift+R",
            image=self.report_icon,
            compound=LEFT,
        )
        self.win.bind("<Control-Shift-R>", lambda x: Report_page(self.win))

        # Account Manu
        self.menu_bar.add_cascade(menu=self.account_menu, label="Account")

        self.icon = Image.open("images//icons//password.png").resize((20, 20))
        self.pass_icon = ImageTk.PhotoImage(self.icon)
        self.account_menu.add_command(
            label="Change Password",
            command=lambda: ChangePassword_page(self.win, UserName),
            accelerator="Ctrl+Shift+P",
            image=self.pass_icon,
            compound=LEFT,
        )
        self.win.bind(
            "<Control-Shift-P>", lambda x: ChangePassword_page(self.win, UserName)
        )

        self.icon = Image.open("images//icons//man.png").resize((20, 20))
        self.user_icon = ImageTk.PhotoImage(self.icon)
        self.account_menu.add_command(
            label="Manage Users",
            command=lambda: Users_page(self.win),
            accelerator="Ctrl+Shift+U",
            image=self.user_icon,
            compound=LEFT,
        )
        self.win.bind("<Control-Shift-U>", lambda x: Users_page(self.win))

        self.icon = Image.open("images//icons//check-out.png").resize((20, 20))
        self.logout_icon = ImageTk.PhotoImage(self.icon)
        self.account_menu.add_command(
            label="Logout",
            command=lambda: self.logout(),
            accelerator="Ctrl+Shift+F4",
            image=self.logout_icon,
            compound=LEFT,
        )
        self.win.bind("<Control-Shift-F4>", lambda x: self.logout())

        # =================== Adding options to the Menubar ===================

        # =================== Creating Frames ===================
        self.main_frame = Frame(
            self.win,
            background=bg_colour,
            width=1000,
            height=600,
            relief=home_frame_releif,
            border=home_frame_border_thickness,
        )
        # =================== Creating Frames ===================

        # =================== Labels ===================
        self.Heading = Label(
            self.win,
            text="Home Page",
            background=bg_colour,
            foreground=fg_colour,
            font=home_heading_font,
        )

        # Log in imgage
        self.home_image = Image.open(
            "./images//homepage_img.jpg"
        ).resize([500, 580])
        self.home_image = ImageTk.PhotoImage(self.home_image)
        self.home_img = Label(
            self.main_frame, image=self.home_image, border=0, background="black"
        ).place(x=0, y=0)

        self.ShortcutsLabel = Label(
            self.main_frame,
            text="SHORTCUTS",
            bg=bg_colour,
            foreground=acent,
            font=ShortcutFont,
        )
        # =================== Labels ===================

        # =================== Buttons ===================
        self.Students_btn = Button(
            self.main_frame,
            width=23,
            text="Students",
            border=home_btn_border_width,
            relief=home_btn_relief,
            font=home_button_font,
            foreground=fg_colour,
            background=bg_colour,
            command=lambda: Student_page(self.win),
        )
        self.Departments_btn = Button(
            self.main_frame,
            width=23,
            text="Departments",
            border=home_btn_border_width,
            relief=home_btn_relief,
            font=home_button_font,
            foreground=fg_colour,
            background=bg_colour,
            command=lambda: Departments_page(self.win),
        )
        self.Courses_btn = Button(
            self.main_frame,
            width=23,
            text="Courses",
            border=home_btn_border_width,
            relief=home_btn_relief,
            font=home_button_font,
            foreground=fg_colour,
            background=bg_colour,
            command=lambda: Courses_page(self.win),
        )
        # =================== Buttons ===================

        # =================== Placing ===================
        self.Heading.pack(pady=40, fill=X)
        x = 550
        y = 120
        xd = 470
        yd = 90
        self.ShortcutsLabel.place(x=x + 80, y=y + 20)
        self.Students_btn.place(x=x, y=y + yd)
        self.Departments_btn.place(x=x, y=y + yd + yd)
        self.Courses_btn.place(x=x, y=y + yd + yd + yd)

        self.main_frame.pack(pady=30)
        # =================== Placing ===================

        if self.utype == "Teacher":
            self.menu_bar.delete(1)
            self.account_menu.delete(1)
            self.Departments_btn.config(state="disabled")
            self.Courses_btn.config(state="disabled")

        self.win.mainloop()

    def logout(self):
        ans = messagebox.askquestion(
            "Confirmation", "Are you sure to Logout ?", parent=self.win
        )
        if ans == "yes":
            self.win.destroy()
            from login_page import Login_page

            Login_page()


if __name__ == "__main__":
    Homepage("", "Admin")
