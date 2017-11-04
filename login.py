#!/usr/bin/env python3

import configuration


def sign_in(login=None, password=None):
    config = configuration.get_default_configuration()
    config.login = login or config.login
    config.password = password or config.password

    print(config)

    # return requests.post(__get_url(), data=__get_login_json(), headers=__get_headers_for_json())


def __get_url():
    return 'https://api.pontomaisweb.com.br/api/auth/sign_in'


def __get_headers_for_json():
    return {'Content-Type': 'application/json;charset=utf-8'}
