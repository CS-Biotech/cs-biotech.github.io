import os
from pelicanconf import *  # noqa: F401, F403

SITEURL = os.environ.get('SITEURL', '')
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
