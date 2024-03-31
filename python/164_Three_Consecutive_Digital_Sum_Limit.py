from functools import cache


@cache
def f(last_three, n_rem):
    if sum(last_three) > 9:
        return 0
    if n_rem == 0:
        return 1
    S = 0
    prev = last_three[1:] if len(last_three) == 3 else last_three
    for d in range(10):
        if d == 0 and n_rem == 20:
            continue
        S += f(prev + (d,), n_rem - 1)
    return S

def p164():
    return f((), 20)
