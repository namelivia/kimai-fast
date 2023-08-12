from kimai.timesheets.timesheets import get_active_timesheets, stop_timesheet

def stop():
    timesheets = get_active_timesheets()
    for timesheet in timesheets:
        stop_timesheet(timesheet['id'])
