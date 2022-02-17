from pickle import TRUE
from py_compile import main
import sys 



import colorama
from colorama import Fore, Back, Style

import time

if len(sys.argv)>1:
    if sys.argv[1] == "update_event":
        import update_event
        update_event.update

    elif sys.argv[1] == "help":
        import info
        info.help

    elif sys.argv[1] == "volunteer_slot":
        import volunteer_slot
        volunteer_slot.volunteer_slot

    elif sys.argv[1] == "book_slot":
        import booking
        booking.book

    elif sys.argv[1] == "cancel_volunteer":
        import cancel_volunteering
        cancel_volunteering.cancel_volunteer

    elif sys.argv[1] == "cancel_booking":
        import cancel_booking
        cancel_booking.cancel_bookings



    elif sys.argv[1] == "list_events":
        import list_events
        list_events.main
       









