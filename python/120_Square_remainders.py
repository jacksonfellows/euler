def max_r(a):
    return max(((a-1)**n + (a+1)**n)%(a**2) for n in range(2*a))

def p120():
    return sum(max_r(a) for a in range(3,1001))
