lst = [line.strip().split(' ') for line in open('3.txt', encoding='UTF8').readlines()]

lst.sort(key=lambda x: x[0][0])
lst.sort(key=lambda x: x[0][1])

print(lst)