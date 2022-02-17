from datetime import datetime, timedelta
from pydoc import describe
from cal_setup import get_calendar_service
import termtables as tt
import list_events


def cancel_bookings():
   """
   
   this function cancels the booked slot.
   
   """
   try:
      service = get_calendar_service()
      
      d = datetime.now().date()
      user_email = input("Please provide your email address:  ")
      list_events.main(list_events.events_list, list_events.events_ID_list)
      print()
      
      book = input('Enter event Id of the event you want to remove yourself from: ')
      
   
      event = service.events().get(calendarId='f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com', eventId=book).execute()


      event['attendees'] = []  #here put the email of the person making the booking 

      update_event = service.events().update(calendarId='f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com', eventId=book, body=event).execute()

      print (update_event['updated'])
      print("You have updated the event")
   except:
      print("Please check your inputs again")
      pass

cancel_bookings()