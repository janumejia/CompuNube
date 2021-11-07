"""
from time import sleep
import json
from kafka import KafkaProducer



producer = KafkaProducer(bootstrap_servers='192.168.50.2:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('Prueba', 'dato 1')
producer.close()
"""

from flask import Flask, request
from time import sleep
import json
import serial
from kafka import KafkaProducer
from datetime import datetime

try:
    port_ref = serial.Serial('COM9', baudrate = 9600)
except serial.SerialException:
    print('port already open')

while True:
    try:
        fecha = datetime.today().strftime('%Y-%m-%d')
        hora = datetime.now().strftime('%H:%M:%S')
        line = port_ref.readline()
        datos = line.decode('utf-8')
        datos = json.loads(datos)
        a = datos['nodo']
        datos['fecha'] = fecha
        datos['hora'] = hora
        print(datos)
        producer = KafkaProducer(bootstrap_servers='192.168.50.2:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send('Prueba', datos)
        producer.close()
    except Exception:
        pass
    except KeyboardInterrupt:
        print('Hello user you have pressed ctrl-c button.')
        exit(0)
