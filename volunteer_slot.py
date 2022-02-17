from datetime import datetime, timedelta
from pydoc import describe
from cal_setup import get_calendar_service
import termtables as tt
from colorama import Fore, Back, Style
import time
import emoji



def volunteer_slot():
   """
   function for handling volunteering of a slot.
   """
   
   service = get_calendar_service()
   try:

        d = datetime.now().date()
        print()
        print("To volunteer, you can create an event by following these steps below")
        print()
        
        summary = input("Enter event summary: ")
        
        description = input("Enter event description: ")
        
        hour  = int(input('At what hour is the event(enter 2 digits only)? '))
        
        Days = int(input("Provide a day , enter 0 for today or 1 for tomorrow: "))
        print()
        duration = float(0.5)
        event_details = datetime(d.year, d.month, d.day, hour)+timedelta(days=Days)
        start = event_details.isoformat()
        end = (event_details+timedelta(hours=duration)).isoformat()

        event_result = service.events().insert(calendarId='primary' and "f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com",
            body={
                "summary": summary,
                "description": description,
                "start": {"dateTime": start, "timeZone": '+2'},
                "end": {"dateTime": end, "timeZone": '+2'},
            }
        ).execute()

        print("Summary: ", event_result['summary'])
        print("Event description: ", event_result['description'])
        print("Starts at: ", event_result['start']['dateTime'])
        print("Ends at: ", event_result['end']['dateTime'])
      
        print(Fore.LIGHTGREEN_EX+"Event created successfully",'\U0001f44d')

   except ValueError:
      print("Please use valid hour inputs, e,g 9,12,13,14,23")
      pass

volunteer_slot()

