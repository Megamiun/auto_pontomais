from pathlib import Path

"""Creates default file variables"""
BASE_DIR = Path('{}/.auto_pontomais'.format(Path.home()))
CONFIG_FILE = BASE_DIR.joinpath('config.yaml')
DB_FILE = BASE_DIR.joinpath('pontomais.db')

"""Creates the folder, if nonexistent"""
BASE_DIR.mkdir(parents=True, exist_ok=True)
