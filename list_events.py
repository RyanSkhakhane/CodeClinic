import datetime
from cal_setup import get_calendar_service

def main():
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   maxDate = (datetime.datetime.now() + datetime.timedelta(days=+6)).isoformat() +'Z'
   events_result = service.events().list(
       calendarId='primary', timeMin=now, timeMax = maxDate,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])
   count =0
   if not events:
       print('No upcoming events found.')
   print()
   print("LIST OF EVENTS\n")
 
   for event in events:
       count +=1
       start = event['start'].get('dateTime', event['start'].get('date'))
       print(count,".",start, '--',event['summary'],'--', 'event ID: ', event["id"])
   print()

if __name__ != '__main__':
   main()