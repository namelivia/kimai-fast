from kimai.api.api import get_url
from kimai.auth.auth import get_headers
import requests

def get_projects_for_customer_id(customer_id):
    return requests.get(
        get_url(f"projects?customer={customer_id}"),
        headers=get_headers()
    ).json()

def create_project(name, customer_id):
    return requests.post(
        get_url("projects"),
        headers=get_headers(),
        data={
            "name": name,
            "customer": customer_id,
            "visible": True,
        }
    ).json()
