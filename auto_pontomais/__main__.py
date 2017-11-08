#!/usr/bin/env python3

import argparse
import getpass

from auto_pontomais.api.clock import clock_in, clock_out
from auto_pontomais.api.login import sign_in
from auto_pontomais.api.status import is_on_journey
from auto_pontomais.persistence.persistence import get_default_user_config
from auto_pontomais.persistence.persistence import get_user_config
from auto_pontomais.persistence.persistence import save_user_config
from auto_pontomais.persistence.persistence import update_default_config


def main(args=None):
    update_default_config(login=args.default_login, password=args.default_password)
    config = __get_config(login=args.login, password=args.password)

    for action in args.actions:
        if action == 'in':
            clock_in(config)
        elif action == 'out':
            clock_out(config)
        elif action == 'status':
            journey_string = "On Journey" if is_on_journey(config) else "Not on Journey"
            print('Status: {}'.format(journey_string))


def __get_config(login, password):
    """Tries to login with given data, if not possible, can ask user for login one time and password multiple times.
    :param login: User login
    :param password: User password
    :return: A DataConfig that has already a valid token
    """
    config = __create_default_config(login=login, password=password)
    while config.login is None:
        login = input('Login: ')
        config = __create_default_config(login=login, password=password)

    if config.token is None:
        config = __login(config)

    """TODO Check for token validity"""
    save_user_config(config)
    return config


def __login(config):
    """Tries to login with given configuration, Assumes that at least the login is correct. Can ask multiple times the
    user for his password in case of fail.
    :param config: Login configuration
    :return: Configuration with login data
    """
    response = sign_in(config)

    while not response.ok:
        print("Couldn't login with user '{}', status code {}. Try again:".format(config.login, response.status_code))
        config = config.overwrite(password=getpass.getpass("Password: "))
        response = sign_in(config)

    json = response.json()
    return config.overwrite(token=json['token'],
                            client=json['client_id'],
                            uid=json['data']['email'])


def __create_default_config(login=None, password=None):
    """Creates a DataConfig of the passed data. If at least the login is passed, tries to get the token from db.
    If there is no login, searches the persisted default user. In both cases, if the user passed any password,
    it substitutes with the passed.
    :param login: User login
    :param password: User password
    :return: The most complete DataConfig possible with persisted and given data
    """
    if login is not None:
        config = get_user_config(login)
    elif password is None:
        config = get_default_user_config()

    return config.overwrite(password=password)


def __parse_args():
    """
    :return: User passed arguments
    """
    parser = argparse.ArgumentParser(description='Clock in and out of pontomais.')
    parser.add_argument(metavar='actions', type=str, help='Actions to do',
                        choices=['in', 'out', 'status'], nargs='+', dest="actions")

    parser.add_argument('-l', '--login', metavar='login', type=str, help='Login for the user')
    parser.add_argument('-p', '--password', metavar='password', type=str,
                        help='Password for the user. will be ignored if user already has a valid token.')

    parser.add_argument('--default-password', metavar='default_password', type=str, dest='default_password',
                        help='Set default password to login when none is given')
    parser.add_argument('--default-login', metavar='default_login', type=str, dest='default_login',
                        help='Set default login to login when none is given')

    return parser.parse_args()


if __name__ == '__main__':
    main(__parse_args())
