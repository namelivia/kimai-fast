from kimai.config.config import (
    get_token
)

def get_headers():
    return {
        "Authorization": f"Bearer {get_token()}",
    
    }
