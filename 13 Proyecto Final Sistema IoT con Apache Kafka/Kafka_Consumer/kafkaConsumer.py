from kafka import KafkaConsumer
from sys import exit
from pymongo import MongoClient
import json

client = MongoClient('127.0.0.1', 27017)

db = client.datos

while True:
    try:

        topic = "Prueba"

        consumer = KafkaConsumer (topic, bootstrap_servers='192.168.50.2:9092')

        for msg in consumer:
            value = msg.value
            datos = value.decode('utf-8')
            datos = json.loads(datos)
            #datos['nodo'] = "comuna_18"
            res = db.datos.insert_one(datos)
            datos2 = {
                "nodo": datos['nodo'],
                "fecha": datos['fecha']
            }
            res2 = db.nodos.find({"nodo": datos2['nodo']})
            contador = 0
            for dato in res2:
                contador = contador + 1
            print(contador)
            if( contador > 0):
                res3 = db.nodos.update_one({"nodo": datos2['nodo']},{"$set":{"fecha": datos2['fecha']}})
            else:
                res4 = db.nodos.insert_one(datos2)


            print("Inserted")
    except Exception:
        print("error")
        pass
    except KeyboardInterrupt:
        print('Hello user you have pressed ctrl-c button.')
        exit(0)