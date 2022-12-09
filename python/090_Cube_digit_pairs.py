import itertools

square_digits = [(x*x//10,x*x%10) for x in range(1,10)]

def extend_die(die):
    ext = set()
    for x in die:
        ext.add(x)
        if x == 6:
            ext.add(9)
        elif x == 9:
            ext.add(6)
    return ext

def can_display_squares(a, b):
    a_ = extend_die(a)
    b_ = extend_die(b)
    for x,y in square_digits:
        if (x in a_ and y in b_) or (y in a_ and x in b_):
            pass
        else:
            return False
    return True

def p90():
    possible_die = tuple(itertools.combinations(range(10), 6))
    n = 0
    for i in range(len(possible_die)):
        for j in range(i, len(possible_die)):
            if can_display_squares(possible_die[i], possible_die[j]):
                n += 1
    return n
