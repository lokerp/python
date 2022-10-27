a = set(int(i) for i in input("Введите первый набор чисел: ").split())
b = set(int(i) for i in input("Введите второй набор чисел: ").split())
c = a & b
print(*sorted(c))
