import os
import re

inputFileName = '4.txt'
outputFileName = '4_4.txt'

def checkFile(fileName):
    if not (os.path.exists(fileName)):
        print(f"Файла {fileName} не существует")
        exit()

checkFile(inputFileName)
checkFile(outputFileName)

with open(inputFileName, encoding = 'utf-8') as file:
    fileInfo = file.read()

chapters = [chapter.strip() for chapter in fileInfo.split('Chapter') if chapter]

file = open(outputFileName, encoding='utf-8', mode='w')
file.write('Оглавление:\n')

for i in chapters:
    words = [word for word in re.split(r'\n+', i)]
    
    number = words[0]
    name = words[1]

    file.write(f'Глава {number}. {name}\n')


file.close()
