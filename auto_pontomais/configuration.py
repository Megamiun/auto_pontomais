from os import linesep
import yaml

CONFIG_DATA_HEADER = '!!python/object:configuration.ConfigData'

CONFIG_FILE_NAME = 'config.yaml'


class ConfigData:
    """User given fields"""
    password = None
    login = None

    """Server given fields"""
    client = None
    token = None
    uid = None

    def __init__(self, login=None, password=None, token=None, uid=None, client=None):
        self.password = password
        self.login = login

        self.client = client
        self.token = token
        self.uid = uid

    def __repr__(self):
        return yaml.dump(self)

    def overwrite(self, login=None, password=None, token=None, uid=None, client=None):
        return ConfigData(password=password or self.password,
                          login=login or self.login,
                          client=client or self.client,
                          token=token or self.token,
                          uid=uid or self.uid)


def get_default_configuration():
    """
    :return: Configuration taken of the configuration yaml file
    """
    file_content = __get_file_content(CONFIG_FILE_NAME)
    return yaml.load(__to_data_config_string(file_content))


def __to_data_config_string(data):
    """
    :param data: Pure yaml info
    :return: String to create new DataConfig instance
    """
    return linesep.join([CONFIG_DATA_HEADER, data])


def __get_file_content(config_file_name):
    """
    :param config_file_name: Configuration file name
    :return: Content of the file
    """
    stream = open(config_file_name, 'r')
    config = stream.read()
    stream.close()
    return config
