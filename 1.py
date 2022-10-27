dict = {'Иванов': 20, 'Сидоров': 68, 'Петров': 26, 'Смирнов': 68}

dict['Соколов'] = 0
dict['Михайлов'] = 141
dict['Фёдоров'] = 12
dict['Новиков'] = 99

dict_length = len(dict.values())
GPA = sum(dict.values()) / dict_length

sortedDict = [*dict.items()]
sortedDict.sort(key=lambda x: x[1])

print(sortedDict)
print(f"Средний балл: {GPA}")

for personIndex in range(dict_length):
    person = sortedDict[personIndex]
    if person[1] > GPA:
        print(f"У {person[0]} балл {person[1]} выше среднего {GPA}")
    if personIndex == 0:
        print(f"Минимальный балл {person[1]} у {person[0]}")
    elif personIndex == dict_length - 1:
        print(f"Максимальный балл {person[1]} у {person[0]}")