import requests

from auto_pontomais import configuration
from auto_pontomais.api import constants, util


def register(login=None, password=None):
    """Try to sign in with the default configuration if custom data not given.
    :param login: Custom login info
    :param password: Custom password info
    :return: Configuration with login data
    """
    config = configuration.get_default_configuration()
    config, response = __do_login(config, login, password)

    while not response.ok:
        print("Couldn't login with user '{}', status code {}. Try again:".format(config.login, response.status_code))
        login = input("Login: ")
        password = input("Password: ")
        config, response = __do_login(config, login, password)

    json = response.json()
    return config.overwrite(token=json['token'],
                            client=json['client_id'],
                            uid=json['data']['email'])


def __do_login(config, login, password):
    """
    :param config: Previous configuration
    :param login: Login string
    :param password: Password string
    :return: Login config and response
    """
    config = config.overwrite(login=login, password=password)
    response = __log_in(config)
    return config, response


def __log_in(config):
    """
    :param config: Configuration data for login
    :return: Response for login request
    """
    return requests.post(constants.LOGIN_ENDPOINT, json=__get_login_json(config), headers=util.get_headers_for_json())


def __get_login_json(config):
    """
    :param config: Configuration with login info
    :return: Dictionary of the info needed.
    """
    return {'login': config.login, 'password': config.password}
