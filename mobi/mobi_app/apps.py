from django.apps import AppConfig


class MobiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobi_app'
    def ready(self):
        import mobi_app.signals 
