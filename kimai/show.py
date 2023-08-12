from kimai.timesheets.timesheets import get_active_timesheets
from datetime import datetime, timezone

def _calculate_time_passed(timestamp_str):
    # This could be also done by the arrow library
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S%z')
    current_time = datetime.now(timezone.utc)
    time_passed = current_time - timestamp
    days = time_passed.days
    hours, remainder = divmod(time_passed.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days > 0:
        time_passed_str = f"{days} days, {hours} hours"
    elif hours > 0:
        time_passed_str = f"{hours} hours, {minutes} minutes"
    elif minutes > 0:
        time_passed_str = f"{minutes} minutes, {seconds} seconds"
    else:
        time_passed_str = f"{seconds} seconds"
    
    return time_passed_str


def show():
    timesheets = get_active_timesheets()
    if len(timesheets) == 0:
        print("No time tracking")
        exit()
    if len(timesheets) > 1:
        print("More than one active timesheet found")
        exit()
    timesheet = timesheets[0]
    customer_name = timesheet['activity']['project']['customer']['name']
    project_name = timesheet['activity']['project']['name']
    activity_name = timesheet['activity']['name']
    duration = _calculate_time_passed(timesheet['begin'])
    print(f"[ {customer_name} ] {project_name} | {activity_name} : {duration}")
    exit()
