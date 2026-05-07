import time
import requests
from datetime import datetime
from .models import Alarma

ESP_IP = "http://192.168.0.122"

#Evita repetir
ejecutadas = set()

estado_persiana = "cerrada"  # "abierta" o "cerrada"


def verificar_alarmas():
    global ejecutadas
    global estado_persiana

    print("Scheduler activo")

    while True:
        ahora = datetime.now()
        hora_actual = ahora.time()
        dia = ahora.weekday()

        alarmas = Alarma.objects.all()

        for alarma in alarmas:

            dias_activos = [
                alarma.lunes,
                alarma.martes,
                alarma.miercoles,
                alarma.jueves,
                alarma.viernes,
                alarma.sabado,
                alarma.domingo,
            ]

            if not dias_activos[dia]:
                continue

            clave_open = f"{alarma.id}-open-{hora_actual.hour}-{hora_actual.minute}"
            clave_close = f"{alarma.id}-close-{hora_actual.hour}-{hora_actual.minute}"

            if (hora_actual.hour == alarma.hora_open.hour and
                    hora_actual.minute == alarma.hora_open.minute):

                if clave_open not in ejecutadas:

                    if estado_persiana != "abierta":
                        print("ABRIENDO")
                        try:
                            requests.get(f"{ESP_IP}/abrir", timeout=2)
                            estado_persiana = "abierta"
                        except:
                            print("Error al abrir")

                    else:
                        print("YA ESTÁ ABIERTA")

                    ejecutadas.add(clave_open)

            if (hora_actual.hour == alarma.hora_close.hour and
                    hora_actual.minute == alarma.hora_close.minute):

                if clave_close not in ejecutadas:

                    if estado_persiana != "cerrada":
                        print("CERRANDO")
                        try:
                            requests.get(f"{ESP_IP}/cerrar", timeout=2)
                            estado_persiana = "cerrada"
                        except:
                            print("Error al cerrar")

                    else:
                        print("YA ESTÁ CERRADA")

                    ejecutadas.add(clave_close)

        #limpieza por m
        if hora_actual.second == 0:
            ejecutadas.clear()

        time.sleep(1)