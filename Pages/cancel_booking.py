from tkinter import *
import os
from .show_seats import show_seats_screen
import json

from colors import *


def cancel_booking_screen(parent, user):
    global cancel_booking
    global _user
    _user = user
    cancel_booking = Toplevel(parent)
    cancel_booking.title("Cancel booking")
    cancel_booking.geometry("700x400")

    bus_options = []

    list_of_files = os.listdir(path="data\\buses")
    for file in list_of_files:
        bus_options.append(file.split(".")[0])

    global value_inside_buses
    value_inside_buses = StringVar(cancel_booking)
    value_inside_buses.set("Select a Bus")

    OptionMenu(cancel_booking, value_inside_buses, *bus_options).pack(pady=20)
    Button(cancel_booking, text="Search this bus", fg="white", bg=primary, command=cancel_seat).pack(pady=20)


def cancel_seat():
    global seat_no
    seat_no = None
    global bus_no_info
    bus_no_info = value_inside_buses.get()
    if bus_no_info != "Select a Bus":
        data = {}
        with open(F"data\\buses\\{bus_no_info}.json", ) as file:
            data = json.load(file)

        for seat, name in data["seats"].items():
            if name == _user:
                Label(cancel_booking,
                      text=F"{_user} You have booked seat no {seat} in this bus would you like to cancel that",
                      fg=danger_dark,padx=5,
                      font=("Calibri", 15)).pack(pady=20)
                seat_no = seat
                Button(cancel_booking, text="Yes, Cancel Booking", fg="white", bg=danger_dark, command=cancel).pack(
                    pady=20)

        if seat_no is None:
            Label(cancel_booking,
                  text=F"{_user} You don't have any reserved seat in this bus",
                  fg=danger_dark,padx=5,
                  font=("Calibri", 15)).pack()


def cancel():
    data = {}
    with open(F"data\\buses\\{bus_no_info}.json", "r") as file:
        data = json.load(file)
    data["seats"][seat_no] = ""
    with open(F"data\\buses\\{bus_no_info}.json", "w") as file:
        json.dump(data, file)
    show_seats_screen(bus_no_info)
    cancel_booking.destroy()
