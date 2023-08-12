from kimai.config.config import (
    get_user,
    get_token
)

def get_headers():
    return {
        "X-AUTH-USER": get_user(),
        "X-AUTH-TOKEN": get_token(),
    }
