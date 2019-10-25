import math
import csv


class KNN:
    def __init__(self, k=1):
        self.x = []
        self.y = []
        self.k = k
        self.cantidad = -1

    def cargarDatos(self, archivo):
        self.x = []
        self.y = []
        f = open(archivo)
        f.readline()
        for line in f:
            line = line.rstrip()
            self.cantidad += 1
            partes = line.split(",")
            self.y.append(partes[-1])
            self.x.append([])
            for p in partes[:-1]:
                self.x[self.cantidad].append(float(p))
        f.close()

    def euclideana(self, punto1, punto2):
        a = 0
        for i in range(0, len(punto1)):
            a += (punto1[i] - punto2[i]) ** 2
        return math.sqrt(a)

    def clasificar(self, punto):
        distancias = []
        for i in range(0, self.cantidad):
            dist = self.euclideana(self.x[i], punto)
            distancias.append((dist, self.y[i]))
        distancias = sorted(distancias, key=lambda x: x[0])
        tags = {}
        for i in range(0, self.k):
            if distancias[i][1] in tags:
                tags[distancias[i][1]] += 1
            else:
                tags[distancias[i][1]] = 1;
        maximo = 0
        maxTag = "";
        for key in tags.keys():
            if tags[key] > maximo:
                maximo = tags[key]
                maxTag = key
        return maxTag

    def cargarTesting(self, archivo):
        print('Entro a cargar testing')
        x = []
        y = []
        cantidad = -1
        f = open(archivo)
        f.readline();
        cont = 0
        for line in f:
            #print('Entro a iterar: ' + str(line))
            cont = cont +1
            line = line.rstrip()
            cantidad += 1
            partes = line.split(",")
            y.append(partes[-1])
            x.append([])
            #print('Imprimeindo x: ' + str(x))
            for p in partes[:-1]:
                x[cantidad].append(float(p))
        f.close()
        # with open('cargarTesting.csv', 'w') as writeFileTrain:
        #     writerTrain = csv.writer(writeFileTrain)
        #     writerTrain.writerows(x)

        print('Terminado,')
        return (x, y)

    def clasificarTodos(self, objetos):
        resultado = []
        #print('Objetos: '+ str(objetos))
        cont = 0
        for objeto in objetos:
            cont = cont +1
            resultado.append(self.clasificar(objeto))
        return resultado

    def accuracy(self, predicciones, reales):
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
        return (tp + tn) / float(tp + tn + fp + fn)

    def f1(self, predicciones, reales):
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


arr_files_test = ['testCrossFold1.csv', 'testCrossFold2.csv', 'testCrossFold3.csv', 'testCrossFold4.csv',
                  'testCrossFold5.csv', 'testCrossFold6.csv', 'testCrossFold7.csv', 'testCrossFold8.csv',
                  'testCrossFold9.csv', 'testCrossFold10.csv']
arr_files_train = ['trainCrossFold1.csv', 'trainCrossFold2.csv', 'trainCrossFold3.csv', 'trainCrossFold4.csv',
                   'trainCrossFold5.csv', 'trainCrossFold6.csv', 'trainCrossFold7.csv', 'trainCrossFold8.csv',
                   'trainCrossFold9.csv', 'trainCrossFold10.csv']




def runK(k):
    file = open(f"salida_entrenamiento_{k}.txt", "w+")

    file.write(f"Entrenamiento con K = {k}\n")
    file.write("\n")
    for j in range(0, 11):
        print('Iniciando con el fold numero: ' + str(j))
        print('Con la k: ' + str(k))
        clasificador = KNN(k)
        file.write(f"Archivo no: {j}\n")
        train_name = arr_files_train[j]
        test_name = arr_files_test[j]

        print(f"K: {k} Fold: {j}")

        clasificador.cargarDatos(train_name)
        (testing, reales) = clasificador.cargarTesting(test_name)
        predicciones = clasificador.clasificarTodos(testing)
        accuracy = clasificador.accuracy(predicciones, reales)
        f1 = clasificador.f1(predicciones, reales)

        print(f"Accuracy: {accuracy}")
        print(f"F1: {f1}\n")

        file.write(f"Accuracy: {accuracy}\n")
        file.write(f"F1: {f1}\n")
        file.write("\n")

    file.close()


runK(4)
