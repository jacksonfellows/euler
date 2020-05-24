def p71():
    a, b = 2, 5
    c, d = 3, 7
    while 1:
        new_a, new_b = a + c, b + d
        if new_b > 1_000_000:
            return a
        a, b = new_a, new_b
