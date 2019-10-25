import csv
import random

def crossFold(testFile, trainFile):
    with open('examen_no corr_notitles.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        pivot = []
        test = []
        train = []

        for row in readCSV:
            pivot.append(row)

        random.shuffle(pivot)

        for i in range(0, int(len(pivot)/2)):
            test.append(pivot[i])
        for j in range(int(len(pivot)/2)+1, len(pivot)):
            train.append(pivot[j])

    with open(testFile, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(test)

    with open(trainFile, 'w') as writeFileTrain:
        writerTrain = csv.writer(writeFileTrain)
        writerTrain.writerows(train)

    csvfile.close()
    writeFile.close()
    writeFileTrain.close()

def main():
    arr_files_test = ['testCrossFold1.csv', 'testCrossFold2.csv', 'testCrossFold3.csv', 'testCrossFold4.csv', 'testCrossFold5.csv','testCrossFold6.csv', 'testCrossFold7.csv', 'testCrossFold8.csv', 'testCrossFold9.csv', 'testCrossFold10.csv']
    arr_files_train = ['trainCrossFold1.csv', 'trainCrossFold2.csv', 'trainCrossFold3.csv', 'trainCrossFold4.csv', 'trainCrossFold5.csv','trainCrossFold6.csv', 'trainCrossFold7.csv', 'trainCrossFold8.csv', 'trainCrossFold9.csv', 'trainCrossFold10.csv']


    for i in range(0, 10):
       crossFold(arr_files_test[i], arr_files_train[i])

main()

