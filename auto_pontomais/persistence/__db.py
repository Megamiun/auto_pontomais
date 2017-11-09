import sqlite3
from enum import Enum

from auto_pontomais.persistence.__constants import DB_FILE
from auto_pontomais.util import get_or_default


class Version(Enum):
    V0_1 = '0.0.1'


def __do_db_action(action):
    """Do an action with a new SQLite connection
    :param action: Function to be executed with a SQLite connection as parameter
    :return: Return of the passed function with a new connection
    """
    conn = sqlite3.connect(str(DB_FILE))

    with conn:
        action_return = action(conn)
        conn.commit()

        return action_return


def __get_version(conn):
    """
    :param conn: SQLite connection
    :return: App version
    """
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='db_version'")

    if cur.fetchone() is None:
        return None

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
    cur.execute('SELECT * FROM user WHERE login = ?', (config.login, ))

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


def __update_db():
    app_version = get_version()

    if app_version is None:
        __do_db_action(lambda conn: __v0_1(conn))


def __v0_1(conn):
    cur = conn.cursor()
    cur.execute('CREATE TABLE db_version (version TEXT)')
    cur.execute(
        """CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        uid TEXT UNIQUE,
        client TEXT,
        token TEXT
        )
        """
    )
    cur.execute("INSERT INTO db_version VALUES (?)", (Version.V0_1.value,))


__update_db()
