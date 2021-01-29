from django.apps import AppConfig


class AwardsConfig(AppConfig):
    name = 'apps.awards'

    def ready(self):
        from . import signals
