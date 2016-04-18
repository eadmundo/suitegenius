"""suitegenius URL Configuration."""
from django.conf.urls import url
from greeter.views import slack

urlpatterns = [
    url(r'^users$', slack.UserList.as_view(), name='list-users'),
    url(r'^post$', slack.PostMessage.as_view(), name='post-message'),
]
