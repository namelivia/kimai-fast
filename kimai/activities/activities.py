from kimai.api.api import get_url
from kimai.auth.auth import get_headers
import requests

def get_activities_for_project_id(project_id):
    return requests.get(
        get_url(f"activities?project={project_id}"),
        headers=get_headers()
    ).json()
