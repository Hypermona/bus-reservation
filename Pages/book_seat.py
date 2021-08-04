from tkinter import *
import os
from .show_seats import show_seats_screen
import json

from colors import *


def book_seat_screen(parent, user):
    global book_seat
    global _user
    _user = user
    book_seat = Toplevel(parent)
    book_seat.title("Book a Seat")
    book_seat.geometry("400x400")

    bus_options = []

    list_of_files = os.listdir(path="data\\buses")
    for file in list_of_files:
        bus_options.append(file.split(".")[0])

    global value_inside_buses
    global value_inside_seats
    value_inside_buses = StringVar(book_seat)
    value_inside_buses.set("Select a Bus")
    value_inside_seats = StringVar(book_seat)
    value_inside_seats.set("Select a seat")

    OptionMenu(book_seat, value_inside_buses, *bus_options).pack(pady=20)
    Button(book_seat, text="Search this bus", fg="white", bg=primary, command=display_seat).pack(pady=20)


def display_seat():
    seats_options = []

    bus_no_info = value_inside_buses.get()
    if bus_no_info != "Select a Bus":
        data = {}
        with open(F"data\\buses\\{bus_no_info}.json", ) as file:
            data = json.load(file)

        for seat, name in data["seats"].items():
            if name == "":
                seats_options.append(seat)

        OptionMenu(book_seat, value_inside_seats, *seats_options).pack(pady=20)
        Label(book_seat, text="").pack()
        Button(book_seat, text="Done", fg="white", bg=primary, command=submit_seat).pack(pady=20)


def submit_seat():
    bus = value_inside_buses.get()
    seat = value_inside_seats.get()
    data = {}
    with open(F"data\\buses\\{bus}.json", "r") as file:
        data = json.load(file)
    data["seats"][seat] = _user
    with open(F"data\\buses\\{bus}.json", "w") as file:
        json.dump(data, file)
    show_seats_screen(bus)
    book_seat.destroy()

