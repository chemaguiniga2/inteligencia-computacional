from sklearn.neural_network import MLPClassifier
import csv
import numpy as np


def cargarDatos(archivo):
    f = open(archivo)
    X = []
    Y = [];
    cantidad = -1;
    for line in f:
        cantidad += 1
        partes = line.split(",");
        X.append([]);
        for parte in partes[:-1]:
            X[cantidad].append(float(parte))
        Y.append(float(partes[-1]))
    return (X, Y)


def cargarTesting(archivo):
    print('Entro a cargar testing')
    x = []
    y = []
    cantidad = -1
    f = open(archivo)
    f.readline();
    for line in f:
        #print('Entro a iterar: ' + str(line))
        line = line.rstrip()
        cantidad += 1
        partes = line.split(",")
        y.append(partes[-1])
        x.append([])
        #print('Imprimeindo x: ' + str(x))
        for p in partes[:-1]:
            x[cantidad].append(float(p))
    f.close()
    return (x, y)

def getAccuracy(predicciones, reales):
    tn = 0
    fn = 0
    tp = 0
    fp = 0
    for i in range(0, len(reales)):
        if reales[i] == "0":
            if predicciones[i] == "0":
                tn += 1
            else:
                fp += 1
        else:
            if predicciones[i] == "0":
                fn += 1
            else:
                tp += 1
    return (tp + tn) / float(tp + tn + fp + fn)


def getF1(predicciones, reales):
    tn = 0
    fn = 0
    tp = 0
    fp = 0
    for i in range(0, len(reales)):
        if reales[i] == "0":
            if predicciones[i] == "0":
                tn += 1
            else:
                fp += 1
        else:  # reales[i]=="1"
            if predicciones[i] == "0":
                fn += 1
            else:
                tp += 1
    recall = tp / float(tp + fn)
    precision = tp / float(tp + fp)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1



file = open(f"salida_neuronal_network.txt", "w+")

for j in range(1, 11):
    clf = MLPClassifier(random_state=42)

    file.write(f"Fold no: {j}\n")
    train_name = f"trainCrossFold{j}.csv"
    test_name = f"testCrossFold{j}.csv"


    X, y = cargarDatos(train_name)
    clf.fit(X, y)
    X_test, y_test = cargarTesting(test_name)
    prediction = clf.predict(X_test)
    #print(prediction)

    accuracy = getAccuracy(prediction, y_test)
    f1 = getF1(prediction, y_test)

    print(f"Accuracy: {accuracy}")
    print(f"F1: {f1}\n")

    file.write(f"Accuracy: {accuracy}\n")
    file.write(f"F1: {f1}\n")
    file.write("\n")
file.close()

