from sklearn.cluster import KMeans
import math
import numpy as np
import random
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt



def cargarDatos(archivo):
    x = []
    cantidad = -1
    f = open(archivo)
    f.readline();
    for line in f:
        line = line.rstrip()
        cantidad += 1
        partes = line.split(",")
        # y.append(float(partes[-1]))
        x.append([])
        for p in partes:
            x[cantidad].append(float(p))
    f.close()
    return x

def distanciaEuclideana(objeto1, objeto2):
    res=0
    for i in range(0, len(objeto1)):
        res+=(objeto1[i]-objeto2[i])**2
    return math.sqrt(res)

def distanciaMenor(centros, objeto1):
    minimo=distanciaEuclideana(centros[0], objeto1)
    for centro in centros[1:]:
        valor=distanciaEuclideana(centro, objeto1)
        if valor<minimo:
            minimo=valor
    return minimo

def clasificar(centros, objetos):
    resultado=[]
    for objeto in objetos:
        resultado.append(distanciaMenor(centros, objeto))
    return resultado

def calcularCentros(x, k):
    cluster = KMeans(n_clusters=k).fit(x);
    return cluster.cluster_centers_



def cargarDataset():
    reales = cargarDatos("real.csv")
    bots = cargarDatos("bot.csv")
    random.shuffle(reales)
    random.shuffle(bots)
    etiquetas=[]
    cantidadReales = len(reales)
    cantidadTraining=math.floor(cantidadReales*.8)
    training=reales[0:cantidadTraining]
    testing=reales[cantidadTraining:]
    for i in range(0, len(testing)):
        etiquetas.append(0)
    testing.extend(bots)
    for i in range(0, len(bots)):
        etiquetas.append(1)
    return (training, testing, etiquetas)


def cargarDatos(archivo):
    x = []
    cantidad = -1
    f = open(archivo)
    f.readline();
    for line in f:
        line = line.rstrip()
        cantidad += 1
        partes = line.split(",")
        # y.append(float(partes[-1]))
        x.append([])
        for p in partes:
            x[cantidad].append(float(p))
    f.close()
    return x

def entrenarClasificar():
    (training, testing, labels)=cargarDataset()
    centros=calcularCentros(training, 10)
    distancias=clasificar(centros, testing)
    (fpr, tpr, t)=roc_curve(labels, distancias)
    prom = 0
    for i in distancias:
        prom += i
    prom /= len(distancias)
    print(prom)
    #print(distancias)
    # plt.figure(1)
    # plt.plot(fpr, tpr)
    # plt.show()
    #print(centros)

def entrenarReal():
    x = cargarDatos("real.csv")
    centros=calcularCentros(x, 10)
    print(centros)

entrenarClasificar()
#entrenarReal()
