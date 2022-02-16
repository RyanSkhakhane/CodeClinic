from pickle import TRUE
from py_compile import main
import sys 

sys.path.append("list_events")

import colorama
from colorama import Fore, Back, Style
import list_events, update_event, cancel_volunteering, booking, volunteer_slot,info,cancel_booking,info,exit

import time

if len(sys.argv)>1:
    if sys.argv[1] == "update_event":
        update_event.update()

    elif sys.argv[1] == "help":
        info.help() 

    elif sys.argv[1] == "exit":
        exit.exiting()

    elif sys.argv[1] == "volunteer_slot":
        volunteer_slot.volunteer_slot()

    elif sys.argv[1] == "book_slot":
        booking.book()

    elif sys.argv[1] == "Cancel_volunteer":
        cancel_volunteering.cancel_volunteer()

    elif sys.argv[1] == "cancel_booking ":
        cancel_booking.cancel_bookings()



    elif sys.argv[1] == "list_events":
        list_events.main(list_events.events_list,list_events.events_ID_list)
       





