from calendar import calendar
import datetime
from cal_setup import get_calendar_service
from prettytable import PrettyTable




events_list = []
events_ID_list = []

def main(events_list,events_ID_list):
   """
   
   function for handling keeping a list of events.

   param: events_list 
        : events_ID_list - this list stores all event's Id's
   
   """
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   maxDate = (datetime.datetime.now() + datetime.timedelta(days=+6)).isoformat() +'Z'
   events_result = service.events().list(
       calendarId='f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com', timeMin=now, timeMax = maxDate,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   events_list.append(events)

   count =0
   if not events:
       print('No upcoming events found.')
   print()
   print("LIST OF CODE CLINICS EVENTS\n")
   
 
   event_list = PrettyTable(['Count','start time','End time','Summary','description','Event Id'])
   for event in events:
       count +=1
       start = event['start'].get('dateTime', event['start'].get('date'))
       end = event['end'].get('dateTime', event['end'].get('date'))
       event_list.add_row([count,start,end,event['summary'],event['description'],event['id']])
       events_ID_list.append(event['id'])

   print(event_list)
   return events_list,events_ID_list 
 

main(events_list,events_ID_list)




