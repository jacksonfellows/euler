from math import isqrt

def sum_consq_sqrs_under(n):
    for i in range(1,isqrt(n)):
        sum = i*i
        j = i + 1
        while 1:
            sum += j*j
            if sum < n:
                yield sum
            else:
                break
            j += 1

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def p125():
    return sum(set(filter(is_palindrome, sum_consq_sqrs_under(10**8))))
