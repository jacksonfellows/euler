def find_solutions(n):
    N = 0
    for x in range(n+1,2*n+1):
        if (n*x) % (x-n) == 0:
            print(x, (n*x) // (x-n))
            N += 1
    return N

def p108():
    return 2*3*5*7*11*13*2*3
