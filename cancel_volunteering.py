from datetime import datetime, timedelta
from pydoc import describe
from cal_setup import get_calendar_service
import termtables as tt
import list_events

import requests

def cancel_volunteer():

   """
   
   function for handling cancelling of a slot.
   
   """
   service = get_calendar_service()

   d = datetime.now().date()
   
   list_events.main(list_events.events_list, list_events.events_ID_list)
   print()
   cancel = input('Enter the event Id you want to cancel: ')
   

   event = service.events().get(calendarId='f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com', eventId=cancel).execute()


   service.events().delete(calendarId='f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com', eventId=cancel).execute()
   print("Slot Cancelled")
     

cancel_volunteer()
