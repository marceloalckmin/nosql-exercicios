import threading
import time
import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['bancoiot']
sensores = db.sensores

def random_temp(nome):
    while True:
        sensorAtivado = sensores.find_one({"nomeSensor": nome})
        if not sensorAtivado["sensorAlarmado"]:
            temp = random.randint(30,40) #gera os valores de temperatura aleatórios
            print(f"{temp}ºC")
            sensores.update_one(
                {'nomeSensor': nome},
                {'$set':{'valorSensor': temp}}
            )
            if temp > 38:
                sensores.update_one(
                    {'nomeSensor': nome},
                    {'$set':{'sensorAlarmado': True}}
                )
                print(f"Atenção! Temperatura muito alta! Verificar sensor {nome}!")
                break
            time.sleep(5)


sensor1 = threading.Thread(target=random_temp, args=("Temp 1",))
sensor2 = threading.Thread(target=random_temp, args=("Temp 2",))
sensor3 = threading.Thread(target=random_temp, args=("Temp 3",))

sensor1.start()
sensor2.start()
sensor3.start()
