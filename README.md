# Neurona

Este neurona fue creada con motivos de una materia.

El modelo empleado fue el perceptron.

La neurona toma los datos desde un archivo csv por especificaciones del maestro.

Para correrla se propone el siguiente codigo en python:

from data import generar_datos as gd
from neurona import Neurona

numdata = 500
name = '.\data1.csv'

gd(numdata,name = name)
n = Neurona(name,0,numdata,[2,3],'mayor',1)
n.train(True,0.9,200)
n.plot_regions()

El codigo funciona de la siguiente manera:
-Mediante la función generar_datos del paquete data crea un archivo csv con el numero de datos especificados y clasificados mediante
  una funcion lineal que se puede modificar en el archivo data.py
-Dada la estructura del archivo se mandan los parametros al constuctor de la neurona.
-para el entrenamiento se puede indicar con False que no se desea vizualizar el grafico de entrenamiento, ademas de poder
  cambiar el "learning rate" y las iteraciones de aprendizaje.
-por ultimo se muestra un grafico de los elementos clasificados por la neurona.
