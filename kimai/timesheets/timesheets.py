from kimai.api.api import get_url
from kimai.auth.auth import get_headers
from datetime import datetime
import requests

def get_active_timesheets():
    return requests.get(
        get_url("timesheets/active"),
        headers=get_headers()
    ).json()

def stop_timesheet(id):
    return requests.get(
        get_url(f"timesheets/{id}/stop"),
        headers=get_headers()
    ).json()

def start_timesheet(activity_id, project_id):
    return requests.post(
        get_url("timesheets"),
        headers=get_headers(),
        data={
            "begin": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "activity": activity_id,
            "project": project_id,
        }
    ).json()
