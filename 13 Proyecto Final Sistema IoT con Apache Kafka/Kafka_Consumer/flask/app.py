from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_pymongo import DESCENDING
from bson.objectid import ObjectId
from flask import render_template
import json
import socket
from bson.objectid import ObjectId
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/datos"
mongo = PyMongo(app)
db = mongo.db

@app.route("/")
def index():
    datos = db.nodos.find()
    data = []
    for dato in datos:
        item = {
            "id": str(dato['_id']),
            "nodo": dato['nodo'],
            "fecha": dato["fecha"]
        }
        data.append(item)
    #return render_template("index.html", data=data)
    return render_template("index.html", data=data)

@app.route("/p")
def prueba():
    datos = db.nodos.find({"_id": ObjectId('61788b20fa010d82009812c3')})
    data = []
    for dato in datos:
        item = {
            "id": str(dato['_id']),
            "nodo": dato['nodo'],
            "humedad": dato['humedad'],
            "temperatura": dato['temperatura'],
            "sensacion": dato['sensacion'],
            "radiacion": dato['radiacion']
        }
        data.append(item)

    return jsonify(data)

@app.route("/datos/<id>")
def main(id):

    datos = db.nodos.find({"_id": ObjectId(id)})
    data = []
    for dato in datos:
        item = {
            "id": str(dato['_id']),
            "nodo": dato['nodo'],
            "fecha": dato["fecha"]
        }
        data.append(item)
        datos = data[0]
    #return render_template("index.html", data=data)
    return render_template("mostrar.html", data = [datos["id"], datos["nodo"], datos["fecha"]])

@app.route("/getDatos/<id>")
def datos(id):

    datos = db.nodos.find({"_id": ObjectId(id)})
    data = []
    for dato in datos:
        item = {
            "nodo": dato['nodo']
        }
        data.append(item)
    dato_s = data[0]
    datos = db.datos.find({"nodo": dato_s['nodo']}).sort([("_id", DESCENDING)]).limit(10)

    datas = []

    for dato in datos:
        item = {
            "id": str(dato['_id']),
            "nodo": dato['nodo'],
            "humedad": dato['humedad'],
            "temperatura": dato['temperatura'],
            "sensacion": dato['sensacion'],
            "radiacion": dato['radiacion'],
            "hora": dato['hora'],
            "fecha": dato['fecha']
        }
        datas.append(item)
    
    return jsonify(datas[::-1])
    
@app.route("/getNodos")
def nodos():
    datos = db.datos.find()
    data = []
    for dato in datos:
        item = {
            "id": str(dato['_id']),
            "nodo": dato['nodo'],
            "fecha": dato["fecha"]
        }
        data.append(item)

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)