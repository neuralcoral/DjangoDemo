from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'streamscheduler'

    def ready(self):
        import streamscheduler.signals  # noqa