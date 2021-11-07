#include "DHT.h"
#include <ArduinoJson.h>
DHT dht(2, DHT11);

//variables
float h = 0.0;
float t = 0.0;
float st = 0.0;
String nodo = "comuna_15";
String json = "";
int a1 = 0;
float r = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  StaticJsonDocument<200> doc;
  // put your main code here, to run repeatedly:
  h = dht.readHumidity();
  t = dht.readTemperature();
  a1 = analogRead(A1);
  r = a1*4.8828125;
  
  if(isnan(h) || isnan(t)){
    Serial.println("Error");  
  }
  st = dht.computeHeatIndex(t, h, false);

  doc["nodo"] = nodo;
  doc["humedad"] = h;
  doc["temperatura"] = t;
  doc["sensacion"] = st;
  doc["radiacion"] = r;
  serializeJson(doc,json);
  Serial.println(json);
  json = "";
  delay(3000);
}
