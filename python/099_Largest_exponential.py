from math import log

pairs = [[int(n) for n in line.strip().split(',')] for line in open('../p099_base_exp.txt').readlines()]

def p99():
    return max(zip(range(len(pairs)), pairs), key=lambda p: log(p[1][0])*p[1][1])[0] + 1
