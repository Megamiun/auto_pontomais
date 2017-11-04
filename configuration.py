#!/usr/bin/env python3

from os import linesep
import yaml

CONFIG_DATA_HEADER = '!!python/object:configuration.ConfigData'

CONFIG_FILE_NAME = 'config.yaml'


class ConfigData:
    def __init__(self, login=None, password=None, token=None):
        self.password = password
        self.login = login
    
    def __repr__(self):
        return yaml.dump(self)


def get_default_configuration():
    file_content = __get_file_content(CONFIG_FILE_NAME)
    return yaml.load(__get_user_config_content(file_content))


def __get_user_config_content(data):
    return linesep.join([CONFIG_DATA_HEADER, data])


def __get_file_content(config_file_name):
    stream = open(config_file_name, 'r')
    config = stream.read()
    stream.close()
    return config
