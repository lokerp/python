lst = [line.strip().split(', ') for line in open('3.txt', encoding='UTF8').readlines()]

lst.sort(key=lambda x: x[::-1])

print(' '.join(([' '.join(i) for i in lst])))