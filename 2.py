import os
import re

inputFileName = '2.txt'
outputFileName = '2_2.txt'

def checkFile(fileName):
    if not (os.path.exists(fileName)):
        print(f"Файла {fileName} не существует")
        exit()

checkFile(inputFileName)
checkFile(outputFileName)

with open(inputFileName, encoding = 'utf-8') as file:
    fileInfo = file.read()

sentences = [sentence.strip() for sentence in (re.findall(r'[^\.\?\!]+', fileInfo))]

wordsNum = int(input("Введите минимальное кол-во слов в предложении: "))
if wordsNum < 0:
    raise ValueError("Неверное значение")

file = open(outputFileName, encoding='utf-8', mode='w')

for sentence in sentences:
    wordsCount = len(re.findall(r'\w+', sentence))
    if wordsCount > wordsNum:
        file.write(f'{sentence}\n')

file.close()