import time
import random
from eventos import EventManager
class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()
            #Notificar el evento
            self.event_manager.notify("evento1",self.data)


    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
    

def get_data(dict_data):
        #Funcion que se encarga de buscar los datos actualizados
        print(f' Datos en tiempo real actualizados: Temperatura actual:{dict_data["temperatura"]} , Humedad actual:{dict_data["humedad"]}')

real_time_data_manager =RealTimeDataManager()
#Suscribir antravez del atributo que es una instancia de la clase EventManager el evento
real_time_data_manager.event_manager.subscribe("evento1",get_data)

# Actualizaciones en tiempo real en segundo plano
import threading
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")
