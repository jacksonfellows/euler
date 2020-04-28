numeral_to_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
val_to_numeral = {v: k for k,v in numeral_to_val.items()}

def read_roman(s):
    n = 0
    p = float('inf')
    for x in s:
        v = numeral_to_val[x]
        if v > p:
            n -= p
            n += v - p
        else:
            n += v
        p = v
    return n

def closest_and_count(n):
    closest = min(filter(lambda v: n >= v, val_to_numeral.keys()), key=lambda v: n - v)
    count = n // closest
    return closest, count

def write_roman(n):
    if n == 0:
        return ''
    closest, count = closest_and_count(n)
    if count == 4 and closest*5 < 1000:
        return val_to_numeral[closest] + val_to_numeral[closest*5] + write_roman(n - closest*count)
    if count == 1 and n - closest > 0 and closest_and_count(n - closest) == (closest//5,4):
        return val_to_numeral[closest//5] + val_to_numeral[closest*2] + write_roman(n - (closest//5)*9)
    return val_to_numeral[closest] * count + write_roman(n - closest*count)

with open('../p089_roman.txt') as f:
    numerals = [line.strip() for line in f.readlines()]

def p89():
    saved_chars = 0
    for numeral in numerals:
        saved_chars += len(numeral) - len(write_roman(read_roman(numeral)))
    return saved_chars
