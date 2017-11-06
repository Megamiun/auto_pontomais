#!/usr/bin/env python3

import configuration
import requests

PONTOMAIS_API = 'https://api.pontomaisweb.com.br/api'


def sign_in(login=None, password=None):
    """Try to sign in with the default configuration if custom data not given.
    :param login: Custom login info
    :param password: Custom password info
    :return: Configuration with login data
    """
    config = configuration.get_default_configuration()
    config, response = do_login(config, login, password)

    while not response.ok:
        print("Couldn't login with user '" + str(config.login) + "', status code "
              + str(response.status_code) + ". Try again:")
        login = input("Login: ")
        password = input("Password: ")
        config, response = do_login(config, login, password)

    return config


def do_login(config, login, password):
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
    return requests.post(__get_sign_in_url(), json=__get_login_json(config), headers=__get_headers_for_json())


def __get_sign_in_url():
    """
    :return: Pontomais sign-in endpoint
    """
    return ''.join([PONTOMAIS_API, '/auth/sign_in'])


def __get_headers_for_json():
    """
    :return: Headers for json requests
    """
    return {'Content-Type': 'application/json'}


def __get_login_json(config):
    """
    :param config: Configuration with login info
    :return: Dictionary of the info needed.
    """
    return {'login': config.login, 'password': config.password}
