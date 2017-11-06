#!/usr/bin/env python3

import argparse

from auto_pontomais.api.login import sign_in
from auto_pontomais.api.clock import clock_in, clock_out
from auto_pontomais.api.status import is_on_journey


def main(args=None):
    login = __get_first_or_default(args.login)
    password = __get_first_or_default(args.password)
    config = sign_in(login=login, password=password)

    for action in args.actions:
        if action == 'in':
            clock_in(config)
        elif action == 'out':
            clock_out(config)
        elif action == 'status':
            journey_string = "On Journey" if is_on_journey(config) else "Not on Journey"
            print('Status: {}'.format(journey_string))


def __get_first_or_default(item, default=None):
    """
    :param item: List to extract item
    :param default: Default value if list is None
    :return: The first item of the list if it exists, else the default value
    """
    return item[0] if item is not None else default


def __parse_args():
    """
    :return: User passed arguments
    """
    parser = argparse.ArgumentParser(description='Clock in and out of pontomais.')
    parser.add_argument(metavar='actions', type=str, help='Actions to do',
                        choices=['in', 'out', 'status'], nargs='+', dest="actions")

    parser.add_argument('-l', '--login', metavar='login', type=str, help='login for the user')
    parser.add_argument('-p', '--password', metavar='password', type=str, help='password for the user')

    return parser.parse_args()


if __name__ == '__main__':
    main(__parse_args())
