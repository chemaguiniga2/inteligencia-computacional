from sklearn import neighbors
import math
import random

def cargarDatos(archivo):
    xNormal = []
    xAnormal = []
    cantidadNormal = -1
    cantidadAnormal = -1
    f = open(archivo)
    f.readline();
    for line in f:
        line = line.rstrip()
        partes = line.split(",")
        etiqueta=int(partes[-1])
        if etiqueta==0:
            cantidadNormal += 1
            xNormal.append([])
            for p in partes:
                xNormal[cantidadNormal].append(float(p))
        else:
            cantidadAnormal+=1
            xAnormal.append([])
            for p in partes:
                xAnormal[cantidadAnormal].append(float(p))
        f.close()
        return (xNormal, xAnormal)

def generarDataset(binario):
    (normal, anormal)=cargarDatos("bank.csv")
    cantidad=len(normal)
    ejemplosNormales=math.floor(cantidad*.8)
    training=normal[:ejemplosNormales]
    etiquetas=[]
    testing=normal[ejemplosNormales:]
    for i in range(0, len(testing)):
        etiquetas.append(0)
    if binario:
        ejemplosAnormales = math.floor(len(anormal)*.8)
        training.extend(anormal[:ejemplosAnormales])
        testing.extend(anormal[ejemplosAnormales:])
        for i in range(0, len(anormal[ejemplosAnormales:])):
            etiquetas.append(1)
    else:
        testing.extend(anormal)
        for i in range(0, len(anormal)):
            etiquetas.append(1)
    return (training, testing, etiquetas)

def probarKNN():
