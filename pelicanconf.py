import random

AUTHOR = 'Wasif Shahzad'
SITENAME = 'The Wasif Report'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Karachi'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
    'archives': None,
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'

DIRECT_TEMPLATES = ['index', 'articles', 'archives', 'tags', 'categories', 'authors']


def random_item(items):
    return random.choice(list(items))


JINJA_FILTERS = {
    'random_item': random_item,
}
