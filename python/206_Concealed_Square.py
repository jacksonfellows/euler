def p206():
    for n in range(int(1e8)):
        x = int(1e9) + n * 10
        if str(x ** 2)[::2] == "1234567890":
            print(x)
            break
