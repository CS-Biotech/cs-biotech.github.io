import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pelicanconf import *  # noqa: F401, F403

SITEURL = os.environ.get('SITEURL', '')
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
