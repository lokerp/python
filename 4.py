number = int(input("Введите десятичное число: "))

def convertToBin(number):
    if number == 0:
        return '0'
    else:
        return str(convertToBin(number // 2)) + str(number % 2)

convertedNum = convertToBin(number)
print(convertedNum)