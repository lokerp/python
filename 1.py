def rec(el, step, counter):
    counter -= 1
    if counter == 0:
        return el
    el *= step
    return rec(el, step, counter)


print(rec(1, 2, 3))