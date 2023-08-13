from kimai.api.api import get_url
from kimai.auth.auth import get_headers
import requests

def get_customers():
    return requests.get(
        get_url("customers"),
        headers=get_headers()
    ).json()

def create_customer(name):
    # I don't care too much about these values
    default_values = {
        "currency": "EUR",
        "country": "ES",
        "timezone": "Europe/Madrid",
    }
    return requests.post(
        get_url("customers"),
        headers=get_headers(),
        data = {
            "name": name,
            "visible": True,
            **default_values,
        }
    ).json()
