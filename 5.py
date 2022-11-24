def rec(nm1, nm2, delitel):
    if nm1 % delitel == 0 and nm2 % delitel == 0:
        return delitel
    if delitel == 2:
        return 0
    return rec(nm1, nm2, delitel-1)

nm1 = 99
nm2 = 54
tmp = rec(nm1, nm2, min(nm1, nm2) - 1)
print(nm1 * nm2 / tmp if tmp else 'Нет НОК')