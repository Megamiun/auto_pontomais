import requests

from auto_pontomais.api.actionError import ActionError
from auto_pontomais.api.constants import REGISTER_ENDPOINT
from auto_pontomais.api.status import is_on_journey
from auto_pontomais.api.util import get_user_headers


def clock_in(config):
    """Try to clock in with the given user
    :param config: User configurations
    """
    if is_on_journey(config):
        print("User {} is already on journey".format(config.uid))
        return

    __toggle(config=config, action='Clock in')


def clock_out(config):
    """Try to clock out with the given user
    :param config: User configurations
    """
    if not is_on_journey(config):
        print("User {} is not on journey".format(config.uid))
        return

    __toggle(config=config, action='Clock out')


def __toggle(config, action):
    response = requests.post(REGISTER_ENDPOINT, headers=get_user_headers(config))

    if not response.ok:
        raise ActionError(action, config.uid, response.status_code)

    print("User uid '{}' - {}".format(config.uid, action))
