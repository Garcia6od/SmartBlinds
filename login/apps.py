from django.apps import AppConfig
import threading

class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'

    def ready(self):
        from .scheduler import verificar_alarmas
        hilo = threading.Thread(target=verificar_alarmas)
        hilo.daemon = True
        hilo.start()