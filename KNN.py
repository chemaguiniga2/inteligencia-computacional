import math
class KNN:
    def __init__(self, k=1):
        self.x=[]
        self.y=[]
        self.k=k
        self.cantidad=-1
    
    def cargarDatos(self,archivo):
        self.x=[]
        self.y=[]
        f=open(archivo)
        f.readline();
        for line in f:
            line=line.rstrip()
            self.cantidad+=1
            partes=line.split(",")
            self.y.append(partes[-1])
            self.x.append([])
            for p in partes[:-1]:
                self.x[self.cantidad].append(float(p))
        f.close()


    def euclideana(self,punto1, punto2):
        a=0
        for i in range(0, len(punto1)):
            a+=(punto1[i]-punto2[i])**2
        return math.sqrt(a)
        
    def clasificar(self,punto):
        distancias=[]
        for i in range(0, self.cantidad):
            dist=self.euclideana(self.x[i], punto)
            distancias.append((dist, self.y[i]))
        distancias=sorted(distancias, key=lambda x: x[0])
        tags={}
        for i in range(0, self.k):
            if distancias[i][1] in tags:
                tags[distancias[i][1]]+=1
            else:
                tags[distancias[i][1]]=1;
        maximo=0
        maxTag="";
        for key in tags.keys():
            if tags[key]>maximo:
                maximo=tags[key]
                maxTag=key
        return maxTag
        
    def cargarTesting(self,archivo):
            x=[]
            y=[]
            cantidad=-1
            f=open(archivo)
            f.readline();
            for line in f:
                line=line.rstrip()
                cantidad+=1
                partes=line.split(",")
                y.append(partes[-1])
                x.append([])
                for p in partes[:-1]:
                    x[cantidad].append(float(p))
            f.close()
            return (x,y)
        
    def clasificarTodos(self, objetos):
        resultado=[]
        for objeto in objetos:
            resultado.append(self.clasificar(objeto))
        return resultado
        
    def accuracy(self, predicciones, reales):
        tn=0
        fn=0
        tp=0
        fp=0
        for i in range(0, len(reales)):
            if reales[i]=="0":
                if predicciones[i]=="0":
                    tn+=1
                else:
                    fp+=1
            else:#reales[i]=="1"
                if predicciones[i]=="0":
                    fn+=1
                else:
                    tp+=1
        return (tp+tn)/float(tp+tn+fp+fn)
                    
    def f1(self, predicciones, reales):
        tn=0
        fn=0
        tp=0
        fp=0
        for i in range(0, len(reales)):
            if reales[i]=="0":
                if predicciones[i]=="0":
                    tn+=1
                else:
                    fp+=1
            else:#reales[i]=="1"
                if predicciones[i]=="0":
                    fn+=1
                else:
                    tp+=1
        recall=tp/float(tp+fn)
        precision=tp/float(tp+fp)
        f1=2*(precision*recall)/(precision+recall)
        return f1


                    
                    
        

#clasificador.cargarDatos("train.csv")
#(testing, reales)=clasificador.cargarTesting("test1.csv")
# clasificador.cargarDatos("trainCrossFold1.csv")
# (testing1, reales1)=clasificador.cargarTesting("testCrossFold1.csv")
# predicciones=clasificador.clasificarTodos(testing1)
# accuracy=clasificador.accuracy(predicciones, reales1)
# f1=clasificador.f1(predicciones, reales1)
# print("Cross Fold 1 accuracy"+ str(accuracy))
# print("Cross fold f1: " + str(f1))


arr_files_test = ['testCrossFold1.csv', 'testCrossFold2.csv', 'testCrossFold3.csv', 'testCrossFold4.csv', 'testCrossFold5.csv']
arr_files_train = ['trainCrossFold1.csv', 'trainCrossFold2.csv', 'trainCrossFold3.csv', 'trainCrossFold4.csv', 'trainCrossFold5.csv']
for ij in range(0, 5):
    clasificador = KNN(1)


    clasificador.cargarDatos(arr_files_train[ij])
    (testing, reales)=clasificador.cargarTesting("twitter.csv")
    predicciones=clasificador.clasificarTodos(testing)
    accuracy=clasificador.accuracy(predicciones, reales)
    f1=clasificador.f1(predicciones, reales)
    print("Cross Fold " + str(ij) +" accuracy"+ str(accuracy))
    print("Cross fold " + str(ij) +" f1: " + str(f1))

# clasificador.cargarDatos("trainCrossFold1.csv")
# (testing3, reales3)=clasificador.cargarTesting("testCrossFold3.csv")
# predicciones=clasificador.clasificarTodos(testing3)
# accuracy=clasificador.accuracy(predicciones, reales3)
# f1=clasificador.f1(predicciones, reales3)
# print("Cross Fold 1 accuracy"+ str(accuracy))
# print("Cross fold f1: " + str(f1))
