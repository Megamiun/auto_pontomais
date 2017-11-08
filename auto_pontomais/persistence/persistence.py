from auto_pontomais.configuration import ConfigData
from auto_pontomais.persistence import config, db


def update_default_config(login, password):
    """Saves default persisted configuration
    :param login: Default user
    :param password: Default password
    """
    config.persist_default_configuration(login, password)


def save_user_config(configuration):
    """Saves configuration for user
    :param configuration: Configuration for user
    """
    db.persist_user_configuration(configuration)


def get_user_config(login):
    """
    :param login: Login id for user
    :return: Configuration with login, and if the register exists on database, token, uid and client
    """
    info = db.get_user_info(login)

    if info is not None:
        token, uid, client = info
        return ConfigData(login=login, token=token, uid=uid, client=client)

    return ConfigData(login=login)


def get_default_user_config():
    """
    :return: Configuration taken of the configuration yaml file
    """
    return config.get_default_configuration()


def __get_version():
    """
    :return: App version for the default database
    """
    return db.get_version()
