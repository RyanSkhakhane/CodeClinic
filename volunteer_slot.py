from datetime import datetime, timedelta
from pydoc import describe
from cal_setup import get_calendar_service
import termtables as tt
from colorama import Fore, Back, Style

def volunteer():
   # creates one timed event for a given date
   service = get_calendar_service()

   d = datetime.now().date()
   summary = input("Enter event summary: ")
   description = input("Enter event description: ")
   hour  = int(input('At what hour is the event(enter 2 digits only)? '))
   Days = int(input("Provide a day , enter 0 for today or 1 for tomorrow: "))
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

   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])
   print("id: ", event_result['id'])
   print(Fore.LIGHTGREEN_EX+"Created event successfully")

if __name__ != "__main__":
    volunteer()