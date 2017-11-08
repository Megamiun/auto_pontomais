import shutil
from os import linesep
from pathlib import Path

import yaml

from auto_pontomais.persistence import CONFIG_FILE

DEFAULT_YAML_FILE = Path('config.default.yaml')
CONFIG_DATA_HEADER = '!!python/object:auto_pontomais.configuration.ConfigData'


def persist_default_configuration(login, password):
    """Saves default persisted configuration
    :param login: Default user
    :param password: Default password
    """
    data = yaml.load(__get_file_content())
    data['login'] = login or data['login']
    data['password'] = password or data['password']

    """TODO Make it so it doesn't completely overwrite file"""
    yaml.dump(data, CONFIG_FILE.open(mode='w'))


def get_default_configuration():
    """
    :return: Configuration taken of the configuration yaml file
    """
    file_content = __get_file_content()
    return yaml.load(__to_data_config_string(file_content))


def __to_data_config_string(data):
    """
    :param data: Pure yaml info
    :return: String to create new DataConfig instance
    """
    return linesep.join([CONFIG_DATA_HEADER, data])


def __get_file_content():
    """
    :return: Content of the file
    """
    if not CONFIG_FILE.is_file():
        shutil.copy(str(DEFAULT_YAML_FILE), str(CONFIG_FILE))

    with CONFIG_FILE.open() as file:
        return file.read()
