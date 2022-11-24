def rec(el, step, counter):
    counter -= 1
    el *= step
    if counter == 0:
        return el
    return rec(el, step, counter)


print(rec(1, 10, 2))