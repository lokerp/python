import os

vhodnoi_file = ('1.txt')
vihodnoi_file = ('1_1.txt')

def checkFile(name):
    if not (os.path.exists(name)):
        print(f"Файла {name} не существует")
        exit()

checkFile(vhodnoi_file)
checkFile(vihodnoi_file)

with open('1.txt') as file:
    fileInfo = file.read()

try:
    vec = [float(i) for i in fileInfo.split(' ')]
except:
    print("Недопустимые данные в файле!")
    exit()

try:
    count = int(input("Введите кол-во элементов для удаления: "))
except:
    print("Недопустимые входные данные!")
    exit()

print(*vec)

if count > len(vec) or count < 0:
    print("Вы ввели неверное значение")
else:
    vec = vec[:len(vec) - count]
    print(*vec)

with open('1_1.txt', 'w') as file:
    file.write(' '.join(map(str, vec)))