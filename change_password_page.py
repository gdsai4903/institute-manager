from settings import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox, Treeview
from PIL import Image, ImageTk
import pymysql


class ChangePassword_page:
    def __init__(self, win, U_name):
        # ================== Defining Global variables ==================
        self.username = U_name
        self.entry_list = []
        self.combobox_list = []
        # =================== Defining Global variables ===================

        # ================== Creating window ==================
        self.Change_pass_win = Toplevel(win)
        # self.Change_pass_win.state("zoomed")
        self.Change_pass_win.config(background=bg_colour)
        # self.Change_pass_win.wm_attributes('-transparentcolor', '#ab23ff')

        self.w = self.Change_pass_win.winfo_screenwidth() - 970
        self.h = self.Change_pass_win.winfo_screenheight() - 600

        # ================== Creating window ==================

        # ================== Setting up the window ==================
        self.Change_pass_win.title("Change Password")
        self.Change_pass_win.geometry("%dx%d+%d+%d" % (self.w, self.h, 480, 330))
        self.W_w = self.Change_pass_win.winfo_width()
        self.W_h = self.Change_pass_win.winfo_height()

        # Background images =================
        self.image = Image.open("images//i4e2.jpg").resize([1920, 1080])

        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.Change_pass_win, image=self.bg_image, border=0)
        self.bg.place(x=0, y=0)

        # Gtb logo imgage
        self.bgimage = Image.open("images//GTBlogo.jpg")

        self.bgimage = ImageTk.PhotoImage(self.bgimage)
        self.gtb_logo_img = Label(self.Change_pass_win, image=self.bgimage).place(
            x=1690, y=893
        )
        # Background images =================

        # self.Change_pass_win.
        self.heading = Label(
            self.Change_pass_win,
            text="CHANGE PASSWORD",
            background=acent,
            foreground=bg_colour,
            font=heading_font,# relief="raised",
            borderwidth=15,
        )
        self.goback_btn = Button(
            self.Change_pass_win,
            text="Bo Back",
            border=2,
            font=button_font,
            foreground=bg_colour,
            background=acent,
            command=lambda: self.Change_pass_win.destroy(),
        )
        # ================== Setting up the window ==================

        # ================== Creating Frames ==================
        self.ChangePassword_Frame = Frame(
            self.Change_pass_win,
            background=bg_colour,
            borderwidth=frame_border_thickness,
            relief=frame_releif,
            width=760,
            height=240,
        )
        # ================== Creating Frames ==================

        # =================== User Frame elements ===================

        self.UserFrameHeader = Label(
            self.ChangePassword_Frame,
            width=50,
            anchor="w",
            text="<<< Change Password >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
            font=header_font,
            background=bg_colour,
            foreground=fg_colour,
        )

        self.OldPasswordLabel = Label(
            self.ChangePassword_Frame,
            text="Old Password :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.OldPasswordEntry = Entry(
            self.ChangePassword_Frame,
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
        self.entry_list.append(self.OldPasswordEntry)

        self.NewPasswordLabel = Label(
            self.ChangePassword_Frame,
            text="New Password :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.NewPasswordEntry = Entry(
            self.ChangePassword_Frame,
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
        self.entry_list.append(self.NewPasswordEntry)

        self.ConfirmPasswordLabel = Label(
            self.ChangePassword_Frame,
            text="Confirm Password :",
            background=bg_colour,
            foreground=fg_colour,
            font=font,
        )
        self.ConfirmPasswordEntry = Entry(
            self.ChangePassword_Frame,
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
        self.entry_list.append(self.ConfirmPasswordEntry)

        # Buttons ============================
        self.ChangePassword = Button(
            self.ChangePassword_Frame,
            text="Change\nPassword",
            width=20,
            height=2,
            foreground=bg_colour,
            background=acent,
            font=button_font,
            cursor=cursor,
            activebackground=bg_colour,
            activeforeground=fg_colour,
            border=0,
            command=self.UpdatePassword,
        )

        # =================== User Frame elements ===================

        # =================== Placing ===================
        # main frame =================
        self.heading.pack(pady=10, fill=X)
        self.goback_btn.place(x=490, y=150)

        f_x = 30
        f_y = 70
        x_diff = 190
        y_diff = 50
        self.UserFrameHeader.place(x=3, y=3)
        self.OldPasswordLabel.place(x=f_x, y=f_y)
        self.OldPasswordEntry.place(x=f_x + x_diff, y=f_y)
        self.NewPasswordLabel.place(x=f_x, y=f_y+y_diff)
        self.NewPasswordEntry.place(x=f_x + x_diff, y=f_y+y_diff)
        self.ConfirmPasswordLabel.place(x=f_x, y=f_y + y_diff+y_diff)
        self.ConfirmPasswordEntry.place(x=f_x + x_diff, y=f_y + y_diff+y_diff)
        self.ChangePassword.place(x=100+f_x + x_diff + x_diff, y=f_y+40)
        
        self.ChangePassword_Frame.pack()



        self.DataBaseConnection()
        self.Clear_all()

        self.Change_pass_win.mainloop()

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
                parent=self.Change_pass_win,
            )

    def UpdatePassword(self):
        if self.NewPasswordEntry.get() == self.ConfirmPasswordEntry.get():
            try:
                query = "update usertable set Password=%s where Username=%s and password=%s"
                rowcount = self.current.execute(query, (self.NewPasswordEntry.get(), self.username, self.OldPasswordEntry.get()))
                self.connection.commit()
                
                if rowcount==1:
                    messagebox.showinfo("Success!!", "User Updated Successfully!", parent= self.Change_pass_win)
                    self.Clear_all()
            except Exception as e:
                messagebox.showerror("Query Error ", "Error in Query:\n" + str(e), parent=self.Change_pass_win)
        else:
            messagebox.showwarning("Failure!", "Passwords Do Not Match", parent=self.Change_pass_win)
    def Clear_all(self):
        for entry in self.entry_list:
            entry.delete(0, END)

if __name__ == "__main__":
    dummy_win = Tk()
    ChangePassword_page(dummy_win, "admin")
