import logging

from pathlib import Path
from decouple import config

from .utils import head_tail, choices, repeat


CURRENT_DIR = Path.cwd()

USERNAME = config('INSTA_USERNAME', default=None)
PASSWORD = config('INSTA_PASSWORD', default=None)

DEBUG = config('INSTA_DEBUG', default=False, cast=bool)

# Uncomment to set a custom User-Agent
# USER_AGENT = None

VERIFY_SSL = config('VERIFY_SSL', default=True, cast=bool)

# Limits requests per second
RATE_LIMITS = {
    '*': [(1, 1)],
    'actions': [(1, 2)],
}

RATE_PERSIST_ENABLED = True
RATE_PERSIST_DIR = CURRENT_DIR / '.onegram/rates'

LOG_SETTINGS = {
    'format': '%(levelname)s:%(name)s: %(message)s',
    'level': logging.DEBUG if DEBUG else logging.INFO,
}

QUERY_CHUNKS = {
    'following': head_tail(20, 10),
    'followers': head_tail(20, 10),
    'posts': repeat(12),
    'feed': repeat(12),
    'likes': head_tail(20, 10),
    'comments': choices(range(20, 40)),
    'explore': repeat(24),
}
