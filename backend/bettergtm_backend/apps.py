from django.apps import AppConfig


class BettergtmBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bettergtm_backend'
    def ready(self):
           import bettergtm_backend.signals