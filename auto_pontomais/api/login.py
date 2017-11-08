import requests

from auto_pontomais.api.constants import LOGIN_ENDPOINT
from auto_pontomais.api.util import get_headers_for_json


def sign_in(config):
    """
    :param config: Configuration data for login
    :return: Response for login request
    """
    return requests.post(LOGIN_ENDPOINT, json=__get_login_json(config), headers=get_headers_for_json())


def __get_login_json(config):
    """
    :param config: Configuration with login info
    :return: Dictionary of the info needed.
    """
    return {'login': config.login, 'password': config.password}
