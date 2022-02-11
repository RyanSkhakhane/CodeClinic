from datetime import datetime, timedelta
from pydoc import describe
from cal_setup import get_calendar_service
import termtables as tt


def main():
   # creates one timed event for a given date
   service = get_calendar_service()

   d = datetime.now().date()
   summary = input("Enter event summary: ")
   description = input("Enter event description: ")
   hour  = int(input('At what hour is the event(enter 2 digits only)? '))
   Days = int(input("Provide a day , enter 0 for today or 1 for tomorrow: "))
   duration = float(input('How long is the event in hours? '))
   event_details = datetime(d.year, d.month, d.day, hour)+timedelta(days=Days)
   start = event_details.isoformat()
   end = (event_details + timedelta(hours=duration)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": summary,
           "description": description,
           "start": {"dateTime": start, "timeZone": '+2'},
           "end": {"dateTime": end, "timeZone": '+2'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])




####################################################################################################
#delete event
# def remove_event(event_id):
    
#     service= get_calendar_service()
#     service.events().delete(calendarId='primary', eventId=event_id).execute()
    
# dd =  '0kd3hkpfu5a0s1cgsdvdkmsni4'
# remove_event(dd) 
