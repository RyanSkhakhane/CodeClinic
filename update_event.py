from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import list_events

def main():
    list_events.main()
    # update the event to tomorrow 9 AM IST
    service = get_calendar_service()

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 9)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=2)).isoformat()
    summary = input('Input event summary:')
    description = input('Input desscription here: ')
    event_result = service.events().update(
        calendarId='primary',
        eventId= input('Copy and paste event ID here: '),
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

