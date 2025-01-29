from math import isqrt, log

def is_power_2(n):
    return 2**int(log(n, 2)) == n
            
def is_perfect2(rt):
    return is_power_2((1 + rt)/2)
            
def p2(lim):
    n = d = 0
    for rt in range(3, isqrt(1 + 4*lim)+1):
        if (rt**2 - 1)%4 != 0:
            continue
        d += 1
        if is_perfect2(rt):
            n += 1
        if n/d < 1/12345:
            return (rt**2 - 1)//4

if __name__ == "__main__":
    print(p2(10**12))