import math
import random
class NB:
    def __init__(self):
        self.unique=0;
        self.pHam=0;
        self.pSpam=0;
        self.palabrasHam={};
        self.palabrasSpam={};
        self.cantidadHam=0;
        self.cantidadSpam=0;
        
    def train(self, mails):
        ham=0;
        spam=0;
        unicas={}
        for mail in mails:
            partes=mail.split("\t")
            if partes[0]=="ham":
                ham+=1
                for palabra in partes[1].split(" "):
                    if palabra not in self.palabrasHam:
                        self.palabrasHam[palabra]=0
                    self.palabrasHam[palabra]+=1
                    self.cantidadHam+=1
                    if palabra not in unicas:
                        unicas[palabra]=0;                    
            else:
                spam+=1
                for palabra in partes[1].split(" "):
                    if palabra not in self.palabrasSpam:
                        self.palabrasSpam[palabra]=0
                    self.palabrasSpam[palabra]+=1
                    self.cantidadSpam+=1
                    if palabra not in unicas:
                        unicas[palabra]=0;
                    
            total=ham+spam
            self.pHam=ham/total
            self.pSpam=spam/total
            self.unique=len(unicas.keys())
                
    def probSpam(self,frase):
            prob=math.log(self.pSpam)
            for palabra in frase.split(" "):
                p=0
                if palabra in self.palabrasSpam:
                    p=self.palabrasSpam[palabra]
                probPalabra=math.log((float(p)+1)/(self.cantidadSpam+self.unique))
                prob*=probPalabra
            return prob
            
    def probHam(self,frase):
            prob=math.log(self.pHam)
            for palabra in frase.split(" "):
                p=0
                if palabra in self.palabrasHam:
                    p=self.palabrasHam[palabra]
                probPalabra=math.log((float(p)+1)/(self.cantidadHam+self.unique))
                prob*=probPalabra
            return prob
            
    def classify(self, phrase):
        spam=self.probSpam(phrase)
        ham=self.probHam(phrase)
        if spam>ham:
            return "spam"
        else:
            return "ham"
    
    def test(self, mails):
        tp=0
        tn=0
        fp=0
        fn=0
        for mail in mails:
            partes=mail.split("\t")
            classFound=self.classify(partes[1])
            if partes[0]=="ham":
                if classFound=="ham":
                    tn+=1
                else:
                    fp+=1
            else:
                if classFound=="spam":
                    tp+=1
                else:
                    fn+=1
        return (tp, tn, fp, fn)

    def fi(self, txt):
        (tp, tn, fp, fn) = self.test(txt)
        recall = tp / float(tp + fn)
        precision = tp / float(tp + fp)
        accuracy = (tp + tn) / float(tp + tn + fp + fn)
        f1 = 2 * (precision * recall) / (precision + recall)
        return (f1, accuracy)




txt = []
f=open("spam", "r")
f1 = f.readlines()
for x in f1:
    txt.append(x)

classifier=NB()
for i in range (1, 11):
    random.shuffle(txt)
    classifier.train(txt)
    (f1, accuracy) = classifier.fi(txt)
    print("Accuracy nº: " +str(i)+ str(accuracy))
    print("F1 nº: " + str(i) +str(f1))
    print("Nº " + str(classifier.classify(txt[2])))


# def cross_fold(txt):
#     classifier = NB()
#     for i in range (1, 11):
#         random.shuffle(txt)
#         (f1, accuracy) = classifier.fi(txt)
#         print(f1, accuracy)
#
# cross_fold(txt)

#
# classifier=NB()
# classifier.train(txt)
# print(classifier.classify(txt[2]))


