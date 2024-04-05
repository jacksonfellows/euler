from matplotlib import pyplot as plt


def ngen():
    s = 290797
    while True:
        s = (s * s) % 50515093
        yield s % 500

from fractions import Fraction


def linegen():
    g = ngen()
    while True:
        yield ((Fraction(next(g)), Fraction(next(g))), (Fraction(next(g)), Fraction(next(g))))

def line_eq(line):
    [[x1,y1],[x2,y2]] = line
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return (m,b)

def vertical(line):
    return line[0][0] == line[1][0]

def between(lo, x, hi):
    if lo == x == hi: return True
    return min(lo, hi) < x < max(lo, hi)

def works(x_int, y_int, line1, line2):
    return between(line1[0][0], x_int, line1[1][0]) and between(line1[0][1], y_int, line1[1][1]) and between(line2[0][0], x_int, line2[1][0]) and between(line2[0][1], y_int, line2[1][1])

def intersection_point(line1, line2):
    if vertical(line2):
        line1, line2 = line2, line1
    if vertical(line1):
        if vertical(line2): return
        [m2,b2] = line_eq(line2)
        x_int = line1[0][0]
        y_int = m2 * x_int + b2
        if works(x_int, y_int, line1, line2):
            return (x_int, y_int)
    else:
        (m1,b1) = line_eq(line1)
        (m2,b2) = line_eq(line2)
        if m1 == m2: return
        x_int = (b2 - b1) / (m1 - m2)
        y_int = m1 * x_int + b1
        if works(x_int, y_int, line1, line2):
            return (x_int, y_int)

def distinct_intersection_points(lines):
    intersection_points = set()
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            p = intersection_point(lines[i], lines[j])
            if p is not None:
                intersection_points.add(p)
    return intersection_points

def p165(N):
    g = linegen()
    lines = [next(g) for _ in range(N)]
    print(lines[0:3])
    return len(distinct_intersection_points(lines))

l1 = ((Fraction(27, 1), Fraction(44, 1)), (Fraction(12, 1), Fraction(32, 1)))
l2 = ((Fraction(46, 1), Fraction(53, 1)), (Fraction(17, 1), Fraction(62, 1)))
l3 = ((Fraction(46, 1), Fraction(70, 1)), (Fraction(22, 1), Fraction(40, 1)))

def test():
    assert n_distinct([l1,l2,l3]) == 1
    g = linegen()
    lines = [next(g) for n in range(5000)]
    for line in lines:
        assert intersection_point(line, line) is None
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            assert intersection_point(lines[i], lines[j]) == intersection_point(lines[j], lines[i])
            assert intersection_point(lines[i], lines[j]) == intersection_point(lines[i][::-1], lines[j][::-1])

def plot(lines):
    for l in lines:
        plt.plot([l[0][0], l[1][0]], [l[0][1], l[1][1]])
    ints = distinct_intersection_points(lines)
    for p in ints:
        plt.plot(p[0], p[1], "ro")
    plt.show()
