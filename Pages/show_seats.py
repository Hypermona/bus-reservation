from tkinter import *
import json
from colors import *


def show_seats_screen(bus_no_info):
    global show_seats
    show_seats = Tk()
    show_seats.title("Bus Seats")
    show_seats.geometry("600x900")

    data = {}

    with open(F"data\\buses\\{bus_no_info}.json", ) as file:
        data = json.load(file)

    count = 0
    col = 0
    row = 2
    Label(show_seats, text=F"Bus No: {data['bus_no']}").grid(row=0, column=0, padx="25", pady="2")
    Label(show_seats, text=F"Driver: {data['driver']}").grid(row=0, column=1, padx="25", pady="2")
    Label(show_seats, text=F"Arrival: {data['arrival']}").grid(row=0, column=2, padx="25", pady="2")
    Label(show_seats, text=F"Departure: {data['departure']}").grid(row=1, column=0, padx="25", pady="2")
    Label(show_seats, text=F"From: {data['from']}").grid(row=1, column=1, padx="25", pady="2")
    Label(show_seats, text=F"To : {data['to']}").grid(row=1, column=2, padx="25", pady="2")
    for seat, name in data["seats"].items():
        if col != 3:
            if name != "":
                Label(show_seats, text=F"{seat} {name}", fg="white", width="10", height="4", bg="green",
                      font=("Calibri", 20)).grid(row=row, column=col, padx="25", pady="2", sticky="W")
            else:
                Label(show_seats, text=F"{seat} {name}", fg="white", width="10", height="4", bg=seat_color,
                      font=("Calibri", 20)).grid(row=row, column=col, padx="25", pady="2", sticky="W")
            col = col + 1
        else:
            row = row + 1
            col = 0
