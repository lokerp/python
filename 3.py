import os

vhodnoi_file = '3.txt'
vihodnoi_file = '3_3.txt'

def transposeMatrix(matrix):
    transpMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transpMatrix[j][i] = matrix[i][j]

    return transpMatrix

def checkFile(file):
    if not (os.path.exists(file)):
        print(f"Файла {file} не существует")
        exit()

checkFile(vhodnoi_file)
checkFile(vihodnoi_file)

with open(vhodnoi_file, encoding = 'utf-8') as file:
    fileInfo = file.read()

matrix = []

for i in fileInfo.split('\n'):
    if len(i) > 0:
        try: 
            row = list(map(int, i.split(' ')))
        except:
            print("Недопустимые данные в файле")
            exit()
        matrix.append(row)
    else:
        print("Вы ввели некорректные данные. Перезапишите файл")
        exit()

newMatrix = transposeMatrix(matrix)

file = open(vihodnoi_file, encoding='utf-8', mode='w')

for row in newMatrix:
    for element in row:
        file.write(f'{str(element)} ')
    file.write('\n')