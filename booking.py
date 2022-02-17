from datetime import datetime, timedelta
from pydoc import describe
from cal_setup import get_calendar_service
import termtables as tt
import list_events


list_eventIds = []


def book():

   """
   
   function for handling booking.
   
   """
   service = get_calendar_service()
   try:
      d = datetime.now().date()
      user_email = input("Please provide your email address:  ")
      list_events.main(list_events.events_list, list_events.events_ID_list)
      print()
      book = input('Enter the event Id you want to book: ')
      
      if book not in list_eventIds:
         list_eventIds.append(book)
         event = service.events().get(calendarId='f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com', eventId=book).execute()
      
         event['attendees'] = [{'email': user_email}]  
         
         
         updated_event = service.events().update(calendarId='f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com', eventId=book, body=event).execute()
         print (updated_event['updated'])

      else:
         print("Event booked")
   except :
      print("Invalid inputs")
      pass
book()   

   




