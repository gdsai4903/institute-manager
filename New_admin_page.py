from settings import *
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


class NewUserPage:
    def __init__(self):
        # ================== Defining Global variables ==================
        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================

        # =================== Creating main window ===================
        self.NewUser_win = Tk()
        self.w = self.NewUser_win.winfo_screenwidth() - 700
        self.h = self.NewUser_win.winfo_screenheight() - 300
        # =================== Creating main window ===================

        # =================== Setting up the window ===================
        self.NewUser_win.title("Regiser New Admin")
        self.NewUser_win.geometry("%dx%d+%d+%d" % (self.w, self.h, 350, 115))
        # self.NewUser_win.state("zoomed")
        self.NewUser_win.option_add("*TearOff", False)
        self.menu_bar = Menu(self.NewUser_win)
        self.NewUser_win.config(menu=self.menu_bar, background=acent)

        # Background Image
        self.image = Image.open(
            "./images//i4e2.jpg"
        ).resize([1920, 1080])
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.NewUser_win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # Gtb logo imgage
        self.bgimage = Image.open(
            "./images//GTBlogo.jpg"
        )
        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.NewUser_win, image=self.bgimage).place(x=1690, y=875)
        # =================== Setting up the window ===================

        # =================== Creating Frames ===================
        self.main_frame = Frame(
            self.NewUser_win,
            background=fg_colour,
            width=1000,
            height=600,
            relief=home_frame_releif,
            border=home_frame_border_thickness,
        )
        
        # Log in imgage
        self.login_image = Image.open(
            "./images//login.jpg"
        ).resize([500, 580])
        self.login_image = ImageTk.PhotoImage(self.login_image)
        self.login_img = Label(self.main_frame, image=self.login_image, border=0).place(x=0, y=0)
        # =================== Creating Frames ===================

        # =================== Labels ===================
        self.Heading = Label(
            self.NewUser_win,
            text="Create New Admin",
            background=bg_colour,
            foreground=fg_colour,
            font=heading_font,
        )
        # =================== Labels ===================
        
        # =================== Main Frame Labels ===================
        self.username_label = Label(self.main_frame, text="Username :", font= login_button_font, background=fg_colour, foreground=bg_colour)
        self.username_entry = Entry(
            self.main_frame,
            width=20,
            font=login_button_font,
            border=entry_border_thickness,
            relief=entry_releif,
        )
        
        self.password_label = Label(self.main_frame, text="Password  :", font= login_button_font, background=fg_colour, foreground=bg_colour)
        self.password_entry = Entry(
            self.main_frame,
            width=20,
            font= login_button_font,
            border=entry_border_thickness,
            relief=entry_releif,
            show="*"
        )
        
        self.Usertype_label = Label(self.main_frame, text="User Type :", font= login_button_font, background=fg_colour, foreground=bg_colour)
        self.Usertype_entry = Combobox(self.main_frame, width=19, font= login_button_font, value=["admin"],state="disabled")
        self.Usertype_entry.set("Admin")
        

        self.Create_btn = Button(
            self.main_frame,
            text="Create Admin",
            width= 15,
            background=bg_colour,
            foreground=fg_colour,
            font=login_button_font,
            relief=btn_relief,
            borderwidth=btn_border_width,
            command=self.Register_user,
        )

        # =================== Placing ===================
        self.Heading.pack(pady=10, fill=X)
        self.main_frame.pack(pady=10)
        
        
        x = 510
        y = 160
        xd = 150
        yd = 70
        self.username_label.place(x=x,y=y)
        self.username_entry.place(x=x+xd,y=y)
        self.password_label.place(x=x,y=y+yd)
        self.password_entry.place(x=x+xd,y=y+yd)
        self.Usertype_label.place(x=x,y=y+yd+yd)
        self.Usertype_entry.place(x=x+xd,y=y+yd+yd)
        self.Create_btn.place(x=x+xd + 20, y=y+yd+yd+yd-20)
        # =================== Placing ===================

        self.DataBaseConnection()

        self.NewUser_win.bind("<Return>",lambda x: self.Register_user())

        self.NewUser_win.mainloop()

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
                parent=self.NewUser_win,
            )


    def Register_user(self):
        if self.validate():
            try:
                query = "insert into usertable values(%s,%s,%s)"
                rowcount = self.current.execute(query, (self.username_entry.get(), self.password_entry.get(), self.Usertype_entry.get()))
                self.connection.commit()
                if rowcount ==1:
                    messagebox.showinfo("Success", "Admin Created Successfully", parent= self.NewUser_win)
                    self.NewUser_win.destroy()
                    from login_page import Login_page
                    Login_page()
                    
            except Exception as e:
                messagebox.showerror("Query Error!!", "Error in Query: \n"+str(e), parent= self.NewUser_win)


    def validate(self):
        if len(self.username_entry.get())<1 or len(self.password_entry.get())<1:
            messagebox.showwarning("Validation failed", "Please enter your username and password", parent= self.NewUser_win)
            return False

        if len(self.password_entry.get())<5:
            messagebox.showwarning("Validation failed", "Password must be atleast 5 letters long", parent= self.NewUser_win)
            return False
            
        return True

    def Clearpage(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.Usertype_entry.delete(0, END)
        
        
        
if __name__ == "__main__":
    NewUserPage()
