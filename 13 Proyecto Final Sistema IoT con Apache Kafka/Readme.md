# Sistema IoT con Apache Kafka, Zookeeper, MongoDB y Flask
<link href="path/to/css/icono-arg.css" rel="stylesheet">

Proyecto final de la asignatura de computación en la nube.

## Contenido

- Kafka_Consumer: Contiene el aplicativo de python que consume los topicos en apache kafka y los almacena en MongoDB y el aplicativo en python Flask para desplegar los eventos de Apache que han sido almacenados en MongoDB. El contenido de esta carpeta va en el SERVIDOR en la nube. 

- Kafka_Producer: Contiene el proyecto en proteus junto con el código en Arduino para simular un nodo de IoT. Además, tiene el aplicativo en python para la recepción de los datos del nodo IoT y se comporta como productor Kafka al publicar eventos de los datos del nodo.

En la guia paso a paso se explica los pasos a seguir para configurar el sistema IoT usando la tecnologia de Apache Kafka. También se incluye un articulo que contiene aspectos teoricos de lo que es apache kafka y zookeeper, asi como un ejemplo de su funcionamiento.

En este video se muestra una DEMO del funcionamiento de este proyecto: https://drive.google.com/file/d/1Xn8rmRCsWxNDfPy5Mm44YWkdVJaEljEx/view?usp=sharing
