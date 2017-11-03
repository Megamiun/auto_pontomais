#!/usr/bin/env python3

from os import linesep
import yaml

class ConfigData:
    def __init__(self, login = None, password = None, token = None):
        self.login = login
        self.password = password
        self.token = token
    
    def __repr__(self):
        return yaml.dump(self)

def get_configuration():
    file_content = __get_file_content(config_file_name)
    user_config = yaml.load(__get_user_config_content(file_content))
    
def __get_user_config_content(data):
    return linesep.join(['!!python/object:__main__.ConfigData', data])  

def __get_file_content(config_file_name):
    stream = open(config_file_name, 'r')
    config = stream.read()
    stream.close()
    return config