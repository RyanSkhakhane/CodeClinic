from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import list_events


def update():

    """
    function for handling updating of events.
    """
    
    list_events.main(list_events.events_list,list_events.events_ID_list)
    
    service = get_calendar_service()

    d = datetime.now().date()
    summary = input('Input event summary: ')
    description = input('Input desscription here: ')
    hour  = int(input('To what hour are you changing the event to(enter 2 digits only)? '))
    Days = int(input("Provide a day , enter 0 for today or 1 for tomorrow: "))
    event_details = datetime(d.year, d.month, d.day, hour)+timedelta(days=Days)
    start = event_details.isoformat()
    duration = float(0.5)
    end = (event_details + timedelta(hours=duration)).isoformat()

    event_result = service.events().update(
        calendarId='primary' and 'f2kecidvtbk56k8j6885l6pkso@group.calendar.google.com',
        eventId= input('Copy and paste event Id here: '),
        body={
        "summary": summary,
        "description": description,
        "start": {"dateTime": start, "timeZone": '+2'},
        "end": {"dateTime": end, "timeZone": '+2'},
        },
    ).execute()

    print("Updated Event\n")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


update()
