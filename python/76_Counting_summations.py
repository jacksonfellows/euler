from functools import lru_cache

def part(n):
    @lru_cache(None)
    def f(n, lim):
        if n < 2:
            return 1
        s = 0
        for i in range(1, min(n,lim)+1):
            s += f(n-i, lim=i)
        return s

    return f(n,n)

def p76():
    return part(100)-1
