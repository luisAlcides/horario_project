from django.apps import AppConfig


class HorariosConfig(AppConfig):
    name = "horarios"

    def ready(self):
        import horarios.signals
