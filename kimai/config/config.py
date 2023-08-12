import os
import yaml

config_path = "~/.config/kimai-fast"
file_name = "config.yml"

def _get_config_from_yaml():
    yaml_file_location = os.path.join(os.path.expanduser(config_path), file_name)
    with open(yaml_file_location, "r") as config_file:
        data = yaml.safe_load(config_file)
        
        user = data.get("user")
        token = data.get("token")
        url = data.get("url")
        
        return user, token, url

def get_user():
    user,_,_ = _get_config_from_yaml()
    return user

def get_token():
    _,token,_ = _get_config_from_yaml()
    return token

def get_url():
    _,_,url = _get_config_from_yaml()
    return url + "/api/"
