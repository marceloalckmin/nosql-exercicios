import threading
import time
import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['bancoiot']
sensores = db.sensores


def random_temp(nome):
    temp = random.randint(30,40)
    print(f"{temp}ºC")
    sensores.update_one(
        {'valorSensor': {'$exists': True}},
        {'valorSensor': temp}
        )  
    if temp > 38:
        sensores.update_one(
            {'sensorAlarmado': {'$exists': True}},
            {'$set':{'sensorAlarmado': True}}
            )
        print(f"Atenção! Temperatura muito alta! Verificar sensor {nome}!")
    time.sleep(5)
      


sensor1 = threading.Thread(target= random_temp, args=" Temp 1")
sensor2 = threading.Thread(target= random_temp, args=" Temp 2")
sensor3 = threading.Thread(target= random_temp, args= "Temp 3")

sensor1.start()
sensor2.start()
sensor3.start()
