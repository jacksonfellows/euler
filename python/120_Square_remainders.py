def p120():
    return sum(a**2 - (2-(a%2))*a for a in range(3,1001))
