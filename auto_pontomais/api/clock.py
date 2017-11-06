import requests

from auto_pontomais.api import constants, util


def clock_in(config):
    """Try to clock in with the given user
    :param config: User configurations
    """
    response = requests.post(constants.REGISTER_ENDPOINT, headers=__get_headers(config))

    if not response.ok:
        raise RegisterError('clock-in', config.uid, response.status_code)

    print("Clocked in with user uid '{}'".format(config.uid))


# def clock_out(config):
#     """Try to clock out with the given user
#     :param config: User configurations
#     """
#     response = requests.post(constants.REGISTER_ENDPOINT, headers=__get_headers(config))
#
#     if not response.ok:
#         raise RegisterError('clock-out', config.uid, response.status_code)
#
#     print("Clocked out with user uid '{}'".format(config.uid))


def __get_headers(config):
    """
    :param config: Current user configurations
    :return: Json with needed headers
    """
    headers = util.get_headers_for_json()
    headers.update({
        'uid': config.uid,
        'client': config.client,
        'token-type': 'Bearer',
        'access-token': config.token
    })
    return headers


class RegisterError(Exception):

    def __init__(self, action, uid, error_code):
        self.uid = uid
        self.action = action
        self.error_code = error_code

    def __str__(self):
        return "Couldn't {} with user uid '{}'. HTTP Status: {}".format(self.action, self.uid, self.error_code)
