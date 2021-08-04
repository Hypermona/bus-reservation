from tkinter import *
from .setup_bus import setup_bus
from .show_seats import show_seats_screen
from .book_seat import book_seat_screen
from .cancel_booking import cancel_booking_screen
from colors import *
import os


def home_screen(user, parent):
    global home
    global _user
    global _parent
    _parent = parent
    _user = user

    home = Tk()
    width = home.winfo_screenwidth()
    height = home.winfo_screenheight()
    home.geometry("%dx%d" % (width, height))
    home.title("Bus Reservation | Home")

    file_count = 0
    list_of_files = os.listdir(path="data\\buses")
    for files in list_of_files:
        file_count = file_count + 1

    Label(home, text=F"Welcome {user} ", bg=primary, width="90", fg="white", height="2", font=("Calibri", 20)).pack(
        side=TOP)

    Label(home, height="5", ).pack(
        side=TOP)
    Button(home, text="Setup Buses", bg=primary, fg="white", width="20", height="2", font=("Calibri", 20),
           command=register_bus).pack()
    Button(home, text="Book a Seat", bg=primary, fg="white", width="20", height="2", font=("Calibri", 20),
           command=register_seat).pack()
    Button(home, text="Show Available Seats", bg=primary, fg="white", width="20", height="2", font=("Calibri", 20),
           command=ask_bus_no).pack()
    Button(home, text="Cancel Booking", bg=primary, fg="white", width="20", height="2", font=("Calibri", 20),
           command=canceling_seat).pack()
    Button(home, text="Logout", bg=primary, width="20", fg="white", height="2", font=("Calibri", 20), command=logout).pack()


def logout():
    home.destroy()
    _parent()


def register_bus():
    setup_bus(home)


def canceling_seat():
    cancel_booking_screen(home, _user)


def register_seat():
    book_seat_screen(home, _user)


def ask_bus_no():
    ask_bus_no_screen = Toplevel(home)
    ask_bus_no_screen.title("Enter Bus no")
    ask_bus_no_screen.geometry("300x300")

    file_options = []
    list_of_files = os.listdir(path="data\\buses")
    for file in list_of_files:
        file_options.append(file.split(".")[0])

    global value_inside
    value_inside = StringVar(ask_bus_no_screen)
    value_inside.set("Select a Bus")

    OptionMenu(ask_bus_no_screen, value_inside, *file_options).pack()
    Label(ask_bus_no_screen, text="").pack()
    Button(ask_bus_no_screen, text="Done", fg="white", bg=primary, command=submit_bus).pack()


def submit_bus():
    bus = value_inside.get()
    show_seats_screen(bus)
