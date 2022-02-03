import colorama
from colorama import Back,Fore,Style
colorama.init(autoreset=True)


def info():
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
|create_event       |- Allows the user to create an event.                                                        |
--------------------+----------------------------------------------------------------------------------------------
|update_event       |- Updates an event, given the event's ID, start and end time.                                |
--------------------+----------------------------------------------------------------------------------------------
|list_events        |- Fetches all calendar events from Code Clinc and User's google calendar.                    |
--------------------+----------------------------------------------------------------------------------------------
|login              |- Logs an active session with google calendar API.                                           |
-------------------------------------------------------------------------------------------------------------------
|                      more functionality comming soon!                                                           |
-------------------------------------------------------------------------------------------------------------------
"""

    print(Help)

if __name__ != '__main__':
    info()
    pass