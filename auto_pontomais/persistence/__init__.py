from auto_pontomais.persistence.__constants import BASE_DIR
from auto_pontomais.persistence.__persistence import *

"""Creates the folder, if nonexistent"""
BASE_DIR.mkdir(parents=True, exist_ok=True)
