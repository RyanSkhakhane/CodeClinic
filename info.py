cmd = ''
def info(cmd):
    # global cmd
    cmd = input()
    Help = """\033[1;32;40mWTC Code Clinic version 0.0.1
These commands are to help navigate the WTC Code Clinic terminal app.
Type help (followed by command name) to see full command details.

+-----------------------------------------------------------------------------------------------------------------+
|COMMAND            |                                   DESCRIPTION                                               |
+-------------------+---------------------------------------------------------------------------------------------+
| help              |- Displays the info currently on screen.                                                     |
+-------------------+---------------------------------------------------------------------------------------------+
|help (+cmd)        |- Display info specific to a command.                                                        |
+-------------------+---------------------------------------------------------------------------------------------+
|view calendar      |- Displays Code Clinic calendar and User calendar stored loacally.                           |
+-------------------+---------------------------------------------------------------------------------------------+
|get calendar       |- Fetches all calendar events from Code Clinc and User's google calendar.                    |
+-------------------+---------------------------------------------------------------------------------------------+
|login              |- Logs an active session with google calendar API.                                           |
+-------------------+---------------------------------------------------------------------------------------------+
|make-booking       |- Displays a list of available time-slots and give the user an option to make a booking.     |
+-----------------------------------------------------------------------------------------------------------------+
"""
    if len(cmd.split(" ")) == 1:
        if cmd.lower() == "help":
            print(Help)

info(cmd)