from tkinter import *
import os
import json



def setup_bus(home):
    global parent

    parent = home
    global setup_bus_screen
    setup_bus_screen = Tk()
    setup_bus_screen.title("Register")
    setup_bus_screen.geometry("800x850")

    # global username
    # global password
    # global username_entry
    # global password_entry
    # username = StringVar()
    # password = StringVar()

    global bus_no
    global driver
    global arrival
    global departure
    global from_
    global to

    global bus_no_entry
    global driver_entry
    global arrival_entry
    global departure_entry
    global from_entry
    global to_entry

    bus_no = StringVar()
    driver = StringVar()
    arrival = StringVar()
    departure = StringVar()
    from_ = StringVar()
    to = StringVar()

    Label(setup_bus_screen, text="Please enter details below", bg="blue").pack()
    Label(setup_bus_screen, text="").pack()
    Label(setup_bus_screen, text="Bus No * ").pack()
    bus_no_entry = Entry(setup_bus_screen, textvariable=bus_no)
    bus_no_entry.pack()

    Label(setup_bus_screen, text="Driver Name * ").pack()
    driver_entry = Entry(setup_bus_screen, textvariable=driver)
    driver_entry.pack()

    Label(setup_bus_screen, text="Arrival Time * ").pack()
    arrival_entry = Entry(setup_bus_screen, textvariable=arrival)
    arrival_entry.pack()

    Label(setup_bus_screen, text="Departure * ").pack()
    departure_entry = Entry(setup_bus_screen, textvariable=departure)
    departure_entry.pack()

    Label(setup_bus_screen, text="From * ").pack()
    from_entry = Entry(setup_bus_screen, textvariable=from_)
    from_entry.pack()

    Label(setup_bus_screen, text="To * ").pack()
    to_entry = Entry(setup_bus_screen, textvariable=to)
    to_entry.pack()

    Label(setup_bus_screen, text="").pack()
    Button(setup_bus_screen, text="Register", width=10, height=1, bg="blue", command=register_bus).pack()


def register_bus():
    bus_no_info = bus_no.get()
    driver_info = driver.get()
    arrival_info = arrival.get()
    departure_info = departure.get()
    from__info = from_.get()
    to_info = to.get()



    dict_data = {
        "bus_no": bus_no_info,
        "driver": driver_info,
        "arrival": arrival_info,
        "departure": departure_info,
        "from": from__info,
        "to": to_info,
        "seats": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": "",
            "10": "",
            "11": "",
            "12": "",
            "13": "",
            "14": "",
            "15": "",
            "16": "",
            "17": "",
            "18": "",
            "19": "",
            "20": "",
        }
    }
    print(dict_data)
    with open(F"data\\buses\\bus_{bus_no_info}.json", "w") as file:
        json.dump(dict_data, file)

    setup_bus_screen.destroy()

    # username_entry.delete(0, END)
    # password_entry.delete(0, END)
    # 
    # Label(setup_bus_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    # Button(setup_bus_screen, text="Goto Home", width=10, height=1,
    #        command=home_screen(user=username_info, primary=primary)).pack()
    # setup_bus_screen.destroy()
    # main_screen.destroy()
