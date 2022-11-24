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

stack = Stack()

[stack.push(i) for i in input()]


flag = True
while flag:
    el = stack.pop()
    if el == None:
        flag = False
    else:
        print(el, end='')