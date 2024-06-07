from settings import *
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk


class Login_page:
    def __init__(self):
        # ================== Defining Global variables ==================
        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================


        # =================== Creating main window ===================
        self.Login_win = Tk()
        self.w = self.Login_win.winfo_screenwidth() - 700
        self.h = self.Login_win.winfo_screenheight() - 300
        # =================== Creating main window ===================


        # =================== Setting up the window ===================
        self.Login_win.title("LOGIN")
        self.Login_win.geometry("%dx%d+%d+%d" % (self.w, self.h, 350, 115))
        # self.Login_win.state("zoomed")

        # Photo
        self.image = Image.open(
            "./images/i4e2.jpg"
        ).resize([1920, 1080])
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.Login_win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # Gtb logo imgage
        self.bgimage = Image.open(
            "./images/GTBlogo.jpg"
        )
        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.Login_win, image=self.bgimage).place(x=1690, y=890)
        # =================== Setting up the window ===================


        # =================== Creating Frames ===================
        self.main_frame = Frame(self.Login_win, background=fg_colour, width=1000, height=600, relief=home_frame_releif, border=home_frame_border_thickness)
        # =================== Creating Frames ===================


        # =================== Labels ===================
        self.Heading = Label(
            self.Login_win,
            text="Login",
            background=bg_colour,
            foreground=fg_colour,
            font=heading_font,
        )
        
        self.username_label = Label(self.main_frame, text="Username", font= login_button_font, background=fg_colour, foreground=bg_colour)
        self.username_entry = Entry(
            self.main_frame,
            width=20,
            font=login_button_font,
            border=entry_border_thickness,
            relief=entry_releif,
        )
        
        self.password_label = Label(self.main_frame, text="Password", font= login_button_font, background=fg_colour, foreground=bg_colour)
        self.password_entry = Entry(
            self.main_frame,
            width=20,
            font= login_button_font,
            border=entry_border_thickness,
            relief=entry_releif,
            show="*"
        )
        
        # Log in imgage
        self.login_image = Image.open(
            "./images//login.jpg"
        ).resize([500, 580])
        self.login_image = ImageTk.PhotoImage(self.login_image)
        self.login_img = Label(self.main_frame, image=self.login_image, border=0).place(x=0, y=0)
        # =================== Labels ===================
        

        # =================== Buttons ===================
        self.login_btn = Button(
            self.main_frame,
            text="Login",
            width= 15,
            background=bg_colour,
            foreground=fg_colour,
            font=login_button_font,
            relief=btn_relief,
            borderwidth=btn_border_width,
            command=self.login
        )
        # =================== Buttons ===================


        # =================== Placing ===================
        self.Heading.pack(pady=10, fill=X)
        x = 510
        y = 200
        xd = 150
        yd = 70
        self.username_label.place(x=x,y=y)
        self.username_entry.place(x=x+xd,y=y)
        self.password_label.place(x=x,y=y+yd)
        self.password_entry.place(x=x+xd,y=y+yd)
        self.login_btn.place(x=x+xd + 20, y=y+yd+yd-20)
        self.main_frame.pack(pady=10)
        # =================== Placing ===================

        self.DataBaseConnection()
        self.Login_win.bind("<Return>",lambda x: self.login())
        self.Login_win.mainloop()
  


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
                parent=self.Login_win,
            )
  
  
    def login(self):
        try:
            qry = "select * from UserTable where Username=%s and Password=%s"
            rowcount = self.current.execute(qry, (self.username_entry.get(), self.password_entry.get()))
            data = self.current.fetchone()
            self.connection.commit()
            if data:
                UserName=data[0]
                UserType=data[2]
                messagebox.showinfo("Success ", "Welcome "+UserType, parent=self.Login_win)
                self.Login_win.destroy()
                from home_page import Homepage
                Homepage(UserName,UserType)
            else:
                messagebox.showwarning("Failure", "Wrong username or Password", parent=self.Login_win)

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.Login_win)


    def clearPage(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        
        
        
if __name__ == "__main__":
    Login_page()
