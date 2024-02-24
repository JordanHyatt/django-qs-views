from django.apps import AppConfig


class DbViewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'db_views'

    def ready(self):
        from db_views import signals