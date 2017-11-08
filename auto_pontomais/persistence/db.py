import sqlite3

from auto_pontomais.persistence import DB_FILE
from auto_pontomais.util import get_or_default


def __do_db_action(action):
    """Do an action with a new SQLite connection
    :param action: Function to be executed with a SQLite connection as parameter
    :return: Return of the passed function with a new connection
    """
    conn = sqlite3.connect(str(DB_FILE))

    with conn:
        return action(conn)


def __get_version(conn):
    """
    :param conn: SQLite connection
    :return: App version
    """
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS db_version (version TEXT)')
    cur.execute('SELECT version FROM db_version')
    return get_or_default(cur.fetchone())


def __get_user_info(conn, login):
    """
    :param conn: SQLite connection
    :param login: User login
    :return: Tuple with token, uid and client
    """
    cur = conn.cursor()
    cur.execute('SELECT token, uid, client FROM user WHERE login = ?', (login, ))
    return cur.fetchone()


def __persist_user_configuration(conn, config):
    """Saves configuration for user
    :param conn: SQLite connection
    :param config: Configuration for user
    """
    cur = conn.cursor()
    cur.execute('SELECT * FROM user u WHERE u.login = ?', (config.login, ))

    user = get_or_default(cur.fetchone())

    if user is None:
        cur.execute('INSERT INTO user (login, token, uid, client) VALUES (?, ?, ?, ?)',
                    (config.login, config.token, config.uid, config.client))
    else:
        cur.execute('UPDATE user SET token = ?, uid = ?, client = ? WHERE login = ?',
                    (config.token, config.uid, config.client, config.login))


def get_version():
    """
    :return: App version for the default database
    """
    return __do_db_action(__get_version)


def get_user_info(login):
    """
    :param login: User login
    :return: User token, if existent, else None
    """
    return __do_db_action(lambda conn: __get_user_info(conn, login))


def persist_user_configuration(config):
    """Saves configuration for user
    :param config: Configuration for user
    """
    return __do_db_action(lambda conn: __persist_user_configuration(conn, config))
