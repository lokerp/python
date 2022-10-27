import time
import re

def help():
    print("! Инструкция\nhelp - Показать инструкцию\nshow - Показать словарь\nshow (автор) - Показать все\
 книги введенного автора\nadd (автор) - Добавить свою книгу\n")

def inputCheck(inputLine):
    cmds = [r'help', r'show(?:$|(?: \w+)+)', r'add(?: \w+)+']
    matchFlag = 0
    for i in cmds:
        if re.fullmatch(i, inputLine):
            matchFlag = 1
    return matchFlag

def printDictionary(dict, author = None):
    if author:
        authorBook = dict.get(author, "Данного автора нет в коллекции")
        print(f"Список книг: {', '.join(authorBook)}")
        return
    print("Текущая коллекция: ")
    for key, item in dict.items():
        print(f"Автор: {key}   Книга: {', '.join(item)}")
    print('*' * 100)

def addBook(dict, author):
    book = input("Введите название книги: ")
    if author not in dict:
        dict[author] = {book}
        return
    dict[author].add(book)

sleepTime = 2
bookDictionary = {
    'Джоан Роулинг': {'Гарри Поттер и узник Азкабана'},
    'Стивен Кинг': {'Зелёная миля'},
    'Маргарет Митчелл': {'Унесённые ветром'},
    'Марио Пьюзо': {'Крёстный отец'},
    'Агата Кристи': {'Десять негритят'},
}
print(f'{"*" * 100}\nВас приветствует интерактивная коллекция лучших книг по мнению livelib.ru')
time.sleep(sleepTime)
print(f'\nМы user-friendly компания, поэтому вы можете добавить своего автора/книгу в коллекцию\n\n{"*" * 100}')
time.sleep(sleepTime)
printDictionary(bookDictionary)
time.sleep(sleepTime)
help()
while True:
    inputLine = input()
    if inputCheck(inputLine) == 0:
        print("Такой команды не существует. Повторите попытку.")
        continue
    if inputLine == "help":
        help()
        continue
    inputLine = inputLine.split()
    if inputLine[0] == "show":
        author = ' '.join(inputLine[1:])
        printDictionary(bookDictionary, author)
    if inputLine[0] == "add":
        author = ' '.join(inputLine[1:])
        addBook(bookDictionary, author)
