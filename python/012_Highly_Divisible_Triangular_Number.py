from math import sqrt


def tris():
    tri = num = 0
    while 1:
        num += 1
        tri += num
        yield tri


def num_factors(n):
    factors = 0
    lim = int(sqrt(n))
    for i in range(1, lim + 1):
        if n % i == 0:
            factors += 2 if i != lim else 1

    return factors


def main():
    for tri in tris():
        if num_factors(tri) > 500:
            print(tri)
            break


if __name__ == '__main__':
    main()
