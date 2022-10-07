from pydoc import doc
import random
import time

def game(n, playerMove, stonesNumber):
    print(f"Ход: {playerMove}\nКамней в куче: {n}")
    time.sleep(waitTime)
    if n < 1:
        if playerMove % 2 == 0: return print("Game Over! You won!")
        else: return print("Game Over! You lose!")
    if playerMove % 2 == 0: stonesNumber = inputStones()
    else: stonesNumber = random.randint(1, 4)
    return game(n - stonesNumber, playerMove + 1, 0)

def inputStones():
    stonesNumber = 0
    while (True):
        stonesNumber = int(input("Введите, сколько камней хотите взять: "))
        if stonesNumber not in range(1, 4):
            print("Введите число от 1 до 3!")
        else:
            break
    return stonesNumber

waitTime = 2
n = random.randint(4, 31)
print(f"Имеется кучка из {n} камней. Каждый игрок берет по очереди 1, 2 или 3 камней.\n\
Выигрывает тот, кто оставляет последний камень сопернику\nУдачи!")
time.sleep(waitTime)
playerFirstMove = random.randint(0, 2)
print("Первый ход - {}".format("Ваш" if playerFirstMove == 0 else "соперника"))
time.sleep(waitTime)
print("Начало игры...")
time.sleep(waitTime)
game(n, playerFirstMove, 0)