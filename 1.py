import math

class Stack: 
    def __init__(self, arr=[]):
        self.arr = arr

    def __str__(self):
        return ' '.join(str(i) for i in self.arr)

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        if len(self.arr) > 0:
            return self.arr.pop(-1)
        else:
            return None

stack = Stack()
word = input('Введите слово: ')
word_length = len(word)
arr = [*word[math.ceil(word_length / 2):]]
arr = arr[::-1]
[stack.push(i) for i in [*word[:math.floor(word_length / 2)]]]


flag = True
counter = math.floor(word_length / 2) - 1
while flag:
    if arr[counter] != stack.pop():
        flag = False
        break
    if counter == 0:
        break
    counter-=1

print('Палиндром' if flag else 'Не палиндром')