#! -*- coding:utf-8 -*-

from sys import maxsize

def max_len_grown(x):
    len_x = len(x)
    max_len = -maxsize
    for i in range(1, len_x):
        result = 1
        for j in range(i, len_x):
            if x[j - 1] < x[j]:
                result = result + 1
        max_len = max(max_len, result)
    return max_len

print(max_len_grown([1, 6, 2, 3, 8, 4, 8, 5, 10]))




