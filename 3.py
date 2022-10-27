import requests
import re
from bs4 import BeautifulSoup

rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')
root = BeautifulSoup(rs.content, 'html.parser')

dict = {}

for tr in root.select('tr[onmouseover]'):
    td_list = [td.text.strip() for td in tr.select('td')]
    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue
    en = td_list[1]
    ru = td_list[5].split(', ')[0]

    dict[ru] = en

print(dict)

words = re.split(r"([A-Za-zА-Яа-яёЁ]+)", input('Введите предложение: '))
sentence = ''

for word in words:
    if re.match(r"[A-Za-zА-Яа-яёЁ]+", word) != None and word.lower() in dict:
        sentence += dict[word.lower()]
    else:
        sentence += word

print(sentence)