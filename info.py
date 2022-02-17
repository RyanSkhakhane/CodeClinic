import colorama
from colorama import Back,Fore,Style
colorama.init(autoreset=True)


def help():
    """
   
   function for displaying the help information for the user.
   
   """
    reset = '\033[39m'
    cmd = Fore.RED + 'COMMAND'
    des = Fore.RED +'DESCRIPTION' 
    credits = Fore.GREEN+ Back.BLACK+'''WTC Code Clinic version 0.0.1
These commands are to help navigate the WTC Code Clinic terminal app.
'''
    Help = f"""{credits}{reset}

-------------------------------------------------------------------------------------------------------------------
|{cmd}{reset}            |                                   {des}{reset}                                               |
--------------------+----------------------------------------------------------------------------------------------
|help               |- Displays the info currently on screen.                                                     |
--------------------+----------------------------------------------------------------------------------------------
|update_event       |- Updates an event, given the event's ID, start and end time.                                |
--------------------+----------------------------------------------------------------------------------------------
|list_events        |- Fetches all calendar events from Code Clinc and User's google calendar.                    |
--------------------+----------------------------------------------------------------------------------------------
|exit               |- Clears session data then closes the app.                                                   |
--------------------+----------------------------------------------------------------------------------------------
|volunteer_slot     |- Allows a volunteer to create an event.                                                     |
--------------------+---------------------------------------------------------------------------------------------
|Cancel_volunteer   |- Allows a volunteer to cancel an event.                                                     |
--------------------+----------------------------------------------------------------------------------------------
|book_slot          |- Allows a student to book an event                                                          |
-------------------------------------------------------------------------------------------------------------------
|cancel_booking     |- Allows a student to cancel a booking                                                       |
-------------------------------------------------------------------------------------------------------------------

"""

    print(Help)

help()
