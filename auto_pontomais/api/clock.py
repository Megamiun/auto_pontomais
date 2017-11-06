import requests

from auto_pontomais.api import constants, util, status
from auto_pontomais.api.actionError import ActionError


def clock_in(config):
    """Try to clock in with the given user
    :param config: User configurations
    """
    if status.is_on_journey(config):
        print("User {} is already on journey".format(config.uid))
        return

    __toggle(config=config, action='Clock in')


def clock_out(config):
    """Try to clock out with the given user
    :param config: User configurations
    """
    if not status.is_on_journey(config):
        print("User {} is not on journey".format(config.uid))
        return

    __toggle(config=config, action='Clock out')


def __toggle(config, action):
    response = requests.post(constants.REGISTER_ENDPOINT, headers=util.get_user_headers(config))

    if not response.ok:
        raise RegisterError(action, config.uid, response.status_code)

    print("User uid '{}' - {}".format(config.uid, action))
