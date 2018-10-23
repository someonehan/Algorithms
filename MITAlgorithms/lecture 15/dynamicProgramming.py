import sys

def createPrice():
    """
    create the price of each length of rod
    :return: dict of price of each length of rod
    """
    i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    P = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    rodprice = dict(zip(i, P))
    return rodprice

def cutRod(n):
    prices = createPrice()
    if n == 0:
        return 0
    best_price = -sys.maxsize
    for cut_len in range(1, n + 1):
        best_price = max(best_price, prices[cut_len] + cutRod(n-cut_len))
        print(cut_len, best_price)
    return best_price

def memoizeCutRod(n):
    r = [-sys.maxsize for _ in range(n)]
    return memoizedCutRodAux(n, r)

def memoizedCutRodAux(n, r):
    prices = createPrice()

    if r[n - 1] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -sys.maxsize
        for i in range(1, n + 1):
            q = max(q, prices[i] + memoizedCutRodAux(n - i, r))

    r.append(q)
    return q

def bottomUpCutRod(n):
    prices = createPrice()
    r = []
    r.append(0)
    for i in range(1, n+1):
        q = -sys.maxsize
        for j in range(1, i + 1):
            q = max(q, prices[j] + r[i - j])
        r.append(q)
        print(r)
    return r[n]

def bottomUpCutRod2(n):
    prices = createPrice()
    r = []
    s = {}
    r.append(0)
    for j in range(1, n + 1):
        q = -sys.maxsize
        for i in range(1, j + 1):
            if q < prices[i] + r[j - i]:
                s[j] = i
                q = prices[i] + r[j - i]
        r.append(q)
    return r[n],s

def printCutRodSolution(n):
    (r,s) = bottomUpCutRod2(n)
    print('the result is:{0}'.format(r))
    print('and the piece is:')
    while n:
        print(s[n])
        n = n - s[n]


if __name__ == "__main__":
    print(printCutRodSolution(6))