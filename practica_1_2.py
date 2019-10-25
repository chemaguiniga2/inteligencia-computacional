#Jose Maria Aguiniga Diaz
#Jorge Alexis Rubio Sumano


import math

def load_file(csv):
    records = []
    with open(csv) as l:
        records = [line.split() for line in l]
    return records
       
def classify(l):

    elemnt_class = 5
    data_set = load_file("train.csv")
    data_set.remove(data_set[0])
    min_distance = 0


    for row in data_set:

        rowClass = row[0].split(",")[2]
        dist = distance(l, row[0].split(","))
        if data_set.index(row) is 0:
            min_distance = dist
            elemnt_class = rowClass
        
        if dist < min_distance:
            min_distance = dist
            elemnt_class = rowClass

    return elemnt_class

def get_clasification(set):

    data_set = load_file(set)
    for row in data_set:
        record = row[0].split(",")
        width = str(record[1])
        height = str(record[0])

        print(height + "," + width + "," + str(classify(record)))
        

def distance(l_1, l_2):
    return math.sqrt(
            math.pow(float(l_1[0]) - float(l_2[0]), 2) +
            math.pow(float(l_1[1]) - float(l_2[1]), 2))

print(classify([3.811663799,4.262188333]))


get_clasification("test1.csv")