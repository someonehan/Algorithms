def fib(n):
    if n == 0 or n == -1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    g = 1
    p = 1
    n -= 1
    while(n >= 2):
        g = p + g
        p = g - p
        n -= 1
    return g



if __name__ == "__main__":
    for i in range(1, 100):
        print(fib2(i))