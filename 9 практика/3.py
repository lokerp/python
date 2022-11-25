import os

inputFileName = '3.txt'
outputFileName = '3_3.txt'

def transposeMatrix(matrix):
    transpMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transpMatrix[j][i] = matrix[i][j]

    return transpMatrix

def checkFile(fileName):
    if not (os.path.exists(fileName)):
        print(f"Файла {fileName} не существует")
        exit()

checkFile(inputFileName)
checkFile(outputFileName)

with open(inputFileName, encoding = 'utf-8') as file:
    fileInfo = file.read()

matrix = []

for i in fileInfo.split('\n'):
    if len(i) > 0:
        row = list(map(int, i.split(' ')))
        matrix.append(row)
    else:
        print("Вы ввели некорректные данные. Перезапишите файл")
        exit()

newMatrix = transposeMatrix(matrix)

file = open(outputFileName, encoding='utf-8', mode='w')

for row in newMatrix:
    for element in row:
        file.write(f'{str(element)} ')
    file.write('\n')