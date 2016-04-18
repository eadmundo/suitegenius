from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
SLACK_TEAM_API_URL = 'https://eadmundo.slack.com/api'

try:
    from .local import *
except ImportError:
    pass
