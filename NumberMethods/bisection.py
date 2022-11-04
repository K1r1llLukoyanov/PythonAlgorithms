def func(x):
    return x ** 2 - 4 * x + 3


def bisection(a, b, e):  # [a;b] - interval of root, e - precision
    if func(a)*func(b) > 0:
        print('func(a) and func(b) values must be with different sign')
        exit(1)

    while 1:
        m = a + (b-a)//2
        v = func(m)
        if v < e:
            return m
        if v*func(a) > 0:
            b = m-1
        else:
            a = m+1


def main():
    print(bisection(2, 4, 0.001))


if __name__ == "__main__":
    main()
