import requests

from auto_pontomais.api import constants, util
from auto_pontomais.api.actionError import ActionError


def is_on_journey(config):
    """
    :return: If token on configuration is on journey
    """
    response = requests.get(constants.STATUS_ENDPOINT, headers=util.get_user_headers(config))

    if not response.ok:
        raise ActionError('User Journey Status', config.uid, response.status_code)

    return response.json()['employee']['work_status']['id'] == 1
