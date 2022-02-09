from cgitb import text
import datetime
from cal_setup import get_calendar_service



list_of_calendars = []

  
def get_list():
   service = get_calendar_service()
   print('      List of calendars\n')
   calendars_result = service.calendarList().list().execute()

   calendars = calendars_result.get('items', [])
  
   if not calendars:
       print('No calendars found.')
   for calendar in calendars:

       summary = calendar['summary']
    
       id = calendar['id']
       primary = "Primary" if calendar.get('primary') else ""
       list_of_calendars.append(id)
       print(summary,"----",id,"----", primary)
       print()
#    print(list_of_calendars)
    
   return list_of_calendars

import datetime

def list_eventts(select):
   service = get_calendar_service()
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   maxDate = (datetime.datetime.now() + datetime.timedelta(days=+7)).isoformat() +'Z'
   events_result = service.events().list(
       calendarId=select, timeMin=now, timeMax = maxDate,
       maxResults=10*10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])
   file = open('calendars.txt', 'w')
   file.write(str(events))
   file.close()
   count =0

   if not events:
       print('No upcoming events found.')
   print()
   print(f"LIST OF EVENTS FOR {select}\n")

   for event in events:
       count +=1
       start = event['start'].get('dateTime', event['start'].get('date'))
       print(count,".",start, '--',event['summary'],'--', 'event ID: ', event["id"])
   return events


def select_calnder(list_of_calendars):
   while True:
    print()   
    select = input("Copy the calendar ID, everything after the ----\n")
    if select in list_of_calendars:
            
        list_eventts(select)
    else:
        print("unavailable")


if __name__ == '__main__':
   calendar = get_list()

   select_calnder(calendar)

   
