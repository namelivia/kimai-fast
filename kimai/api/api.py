from kimai.config.config import get_url as get_base_url

def get_url(path):
    return get_base_url() + path
