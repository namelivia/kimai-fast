from kimai.api.api import get_url
from kimai.auth.auth import get_headers
import requests

def get_projects():
    return requests.get(
        get_url("projects"),
        headers=get_headers()
    ).json()

def create_project(name):
    return requests.post(
        get_url("projects"),
        headers=get_headers(),
        data={
            "name": name,
            "customer": 1, # TODO: Choose customer
            "visible": True,
        }
    ).json()
