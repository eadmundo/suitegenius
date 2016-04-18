"""Slack proxy views."""
from django.conf import settings
from rest_framework_proxy.views import ProxyView


class SlackProxyView(ProxyView):
    """Slack proxy base class."""

    proxy_host = settings.SLACK_TEAM_API_URL


class UserList(SlackProxyView):
    """List users."""

    source = '/users.list'


class PostMessage(SlackProxyView):
    """Post a message."""

    source = '/chat.postMessage'


class OAuthAccess(SlackProxyView):
    """Obtain an ouath access token."""

    source = '/oauth.access'
