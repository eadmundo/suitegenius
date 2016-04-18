from rest_framework import authentication
from rest_framework import exceptions


class SlackAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # get token from header
        token = request.META.get('X-SLACK-TOKEN')
        # no token - don't try and auth
        if not token:
            return None

        try:
            # see if this token is any good
            r = request.get('https://<team>.slack.com/api/auth.test?token=<token>')
            auth_json = r.json()

            # check for an error raise exception
            # if we don't have an exception, pull out the user_id
            # will need to create a user object to return
            # django user object?
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
