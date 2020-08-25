def rects(m, n):
    return m*(m+1)//2 * n*(n+1)//2

def p85():
    min_d = float('inf')
    min_area = None
    for m in range(1,1000):
        for n in range(m,1000):
            d = abs(rects(m, n) - 2000000)
            if d < min_d:
                min_d = d
                min_area = m * n
    return min_area

print(p85())
