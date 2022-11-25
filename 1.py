import os

inputFileName = ('1.txt')
outputFileName = ('1_1.txt')

def checkFile(fileName):
    if not (os.path.exists(fileName)):
        print(f"Файла {fileName} не существует")
        exit()

checkFile(inputFileName)
checkFile(outputFileName)

with open('1.txt') as file:
    fileInfo = file.read()

vector = [float(i) for i in fileInfo.split(' ')]

delElCount = int(input("Введите кол-во элементов для удаления: "))

print(*vector)

if delElCount > len(vector) or delElCount < 0:
    print("Вы ввели неверное значение")
else:
    vector = vector[:len(vector) - delElCount]
    print(*vector)

with open('1_1.txt', 'w') as file:
    file.write(' '.join(map(str, vector)))