import os
import re

vhodnoi_file = '2.txt'
vihodnoi_file = '2_2.txt'

def checkFile(file):
    if not (os.path.exists(file)):
        print(f"Файла {file} не существует")
        exit()

checkFile(vhodnoi_file)
checkFile(vihodnoi_file)

with open(vhodnoi_file, encoding = 'utf-8') as file:
    fileInfo = file.read()

try:
    sentences = [sentence.strip() for sentence in (re.findall(r'[^\.\?\!]+', fileInfo))]
except:
    raise ValueError("Недопустимые данные в файле!")

wordsNum = int(input("Введите минимальное кол-во слов в предложении: "))
if wordsNum < 0:
    raise ValueError("Неверное значение")

file = open(vihodnoi_file, encoding='utf-8', mode='w')

for sentence in sentences:
    wordsCount = len(re.findall(r'\w+', sentence))
    if wordsCount > wordsNum:
        file.write(f'{sentence}\n')

file.close()