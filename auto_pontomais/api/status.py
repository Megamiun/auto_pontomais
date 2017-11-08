import requests

from auto_pontomais.api.actionError import ActionError
from auto_pontomais.api.constants import STATUS_ENDPOINT
from auto_pontomais.api.util import get_user_headers


def is_on_journey(config):
    """
    :return: If token on configuration is on journey
    """
    response = requests.get(STATUS_ENDPOINT, headers=get_user_headers(config))

    if not response.ok:
        raise ActionError('User Journey Status', config.uid, response.status_code)

    return response.json()['employee']['work_status']['id'] == 1
