from django.apps import AppConfig


class GreeterAppConfig(AppConfig):

    name = 'greeter'

    def ready(self):

        # import signal handlers
        from . import signals
