import importlib.util
from pathlib import Path

# pkg_resources is absent in modern uv venvs; locate the theme without importing alchemy
_spec = importlib.util.find_spec('alchemy')
_ALCHEMY_PATH = str(Path(_spec.origin).parent)

AUTHOR = ''
SITENAME = 'Hybrid Modules to Bridge Biotechnology and Computer Science'
SITEURL = ''
SITESUBTITLE = 'Bridging Biotechnology and Computer Science at the University of Toronto'

PATH = 'content'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = _ALCHEMY_PATH

# Single-page site: disable the article-list index so the page below owns index.html
DIRECT_TEMPLATES = []
DISPLAY_PAGES_ON_MENU = False

THEME_TEMPLATES_OVERRIDES = ['templates']

LINKS = ()
SOCIAL = ()
DEFAULT_PAGINATION = False
