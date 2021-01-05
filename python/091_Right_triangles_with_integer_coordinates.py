from itertools import combinations, product

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def is_right(x1, y1, x2, y2):
    return dot([x1,y1], [x2,y2]) == 0 or dot([x1,y1], [x1-x2,y1-y2]) == 0 or dot([x1-x2,y1-y2], [x2,y2]) == 0

def point_pairs(h):
    return map(lambda ps: ps[0]+ps[1], combinations(filter(lambda p: p[0] != 0 or p[1] != 0, product(range(h+1), range(h+1))), 2))

def p91():
    n = 0
    for x1,y1,x2,y2 in point_pairs(50):
        if is_right(x1,y1,x2,y2):
            n += 1
    return n
