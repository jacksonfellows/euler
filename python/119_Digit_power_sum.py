def dsum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def p119():
    elems = []
    for digit_sum in range(1,100):
        if dsum(digit_sum) == 1:
            continue
        for p in range(1,100):
            n = digit_sum ** p
            n_digit_sum = dsum(n)
            if n_digit_sum == digit_sum and n > 10:
                elems.append(n)
    return sorted(elems)[29]
