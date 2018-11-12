

def naive_matching(t, p):
    m, n = len(p), len(t)
    i = j = 0
    while i < n and j < m:
        if t[i] == p[j]:
            i, j = i + 1, j + 1
        else:
            j, i = 0, i - j + 1