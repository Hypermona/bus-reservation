# import modules

from tkinter import *
import os
from Pages import home_screen
from PIL import Image

primary = "#F536CF"  # "#492540"
secondary = "#f6ea8c"
danger_dark = "#c03546"
danger_light = "#f26d5b"


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(F"data\\users\\{username_info}", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(register_screen, text="Goto Home", width=10, height=1,
           command=home_screen(user=username_info, parent=home_screen)).pack()
    register_screen.destroy()
    main_screen.destroy()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir(path="data\\users")
    if username1 in list_of_files:
        file1 = open(F"data\\users\\{username1}", "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Button(login_screen, text="Goto Home", width=10, height=1,
                   command=home_screen(user=username1, parent=main_account_screen)).pack()
            login_screen.destroy()
            main_screen.destroy()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    # Add image file

    width = main_screen.winfo_screenwidth()
    height = main_screen.winfo_screenheight()
    main_screen.geometry("%dx%d" % (width, height))
    main_screen.title("Bus Reservation")

    print("Please wait, we are launching...")
    image_file = "images/bus_bg_t.gif"

    info = Image.open(image_file)
    frames = info.n_frames
    bg = [PhotoImage(file=image_file, format=F"gif -index {i}") for i in range(frames)]

    def animation(count):
        im = bg[count]
        gif_lable.configure(image=im)
        count += 1
        if count == frames:
            count = 0

        main_screen.after(20, lambda: animation(count))

    gif_lable = Label(image="")
    gif_lable.pack()
    animation(0)

    # # Create Canvas
    # canvas1 = Canvas(main_screen, width=500,
    #                  height=500)
    #
    # canvas1.pack(fill="both", expand=True)

    # Display image
    # canvas1.create_image(0, 0, image=bg,
    #                      anchor="nw")
    # btnlogin = Button(main_screen, text="Login", height="2", width="30", bg=primary, fg="white", font=("Calibri", 15),
    #                   command=login)
    # canvas_log = canvas1.create_window(600, 250,
    #                                    anchor="nw",
    #                                    window=btnlogin)
    # btnregister = Button(text="Register", height="2", width="30", bg=primary, fg="white", font=("Calibri", 15),
    #                      command=register)
    # canvas_reg = canvas1.create_window(600, 350, anchor="nw", window=btnregister)

    # Label(text="Select Your Choice", bg=primary, width="300", fg="white", height="2", font=("Calibri", 20)).pack()
    # Label(text="", height="10").pack()
    Button(text="Login", height="2", width="30", bg=primary, fg="white", font=("Calibri", 15), command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", bg=primary, fg="white", font=("Calibri", 15),
           command=register).pack()

    main_screen.mainloop()


main_account_screen()
