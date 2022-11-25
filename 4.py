import os
import re

vhodnoi_file = '4.txt'
vihodnoi_file = '4_4.txt'

def checkFile(file):
    if not (os.path.exists(file)):
        print(f"Файла {file} не существует")
        exit()

checkFile(vhodnoi_file)
checkFile(vihodnoi_file)

with open(vhodnoi_file, encoding = 'utf-8') as file:
    fileInfo = file.read()

try:
    chapters = [chapter.strip() for chapter in fileInfo.split('Chapter') if chapter]
except:
    print("Недопустимые данные в файле")
    exit()

file = open(vihodnoi_file, encoding='utf-8', mode='w')
file.write('Оглавление:\n')

for i in chapters:
    words = [word for word in re.split(r'\n+', i)]
    
    number = words[0]
    name = words[1]

    file.write(f'Глава {number}. {name}\n')


file.close()
