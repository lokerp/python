n = int(input('Введите количество членов геометрической прогрессии: '))
if (n < 1):
    print("Вы ввели неверное значение, перезапустите программу!")

firstEl = float(input('Введите первый член геометрической прогрессии: '))
denominator = float(input('Введите знаменатель геометрической прогрессии: '))
sum = firstEl

def getGeometricProgressionSum(n, element, denominator, sum):
    if n <= 0:
        return sum

    el = element * denominator
    sum += el

    return getGeometricProgressionSum(n - 1, el, denominator, sum)

sum = getGeometricProgressionSum(n - 1, firstEl, denominator, sum)

print(sum)