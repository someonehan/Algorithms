#! -*- coding:utf-8 -*-

"""
Longest palindrome subsequence
A Palindrome is a nonempty string over some alphabet that reads the same forward and backward
Give an efficient algorithm to find the longest palindrome that is a subsequence of a input string
for example 'character', your algorithm should return 'carac'
what's the running time of your algorithm
"""

import numpy as np

result = []


def set_memorize(c, head, tail):
    m = np.zeros((tail + 1, tail + 1), dtype=int)
    res = find_longest_palindrome(c, head, tail, m)
    return res, m


def find_longest_palindrome(c, head, tail, m):
    if head > tail:
        return 0
    if m[head][tail] != 0:
        return m[head][tail]

    if head == tail:
        return 1
    elif c[head] == c[tail]:
        m[head][tail] = find_longest_palindrome(c, head + 1, tail - 1, m) + 2;
    else:
        m[head][tail] = max(find_longest_palindrome(c, head + 1, tail, m),
                     find_longest_palindrome(c, head, tail-1, m))
    return m[head][tail]

def find_longest_palindrome_bottom_up(c):
    len_c = len(c)

    m = np.zeros((len_c, len_c), dtype=int)
    # for i in range(len_c):
    #     m[i][i] = 1

    print(m)
    for i in range(0, len_c):
        for j in range(1, len_c):
            max_len = m[i][j-1]
            if c[i] == c[j]:
                m[i][j] = max_len + 1
            else:
                m[i][j] = max_len
    print(m)
    return m[len_c-1][len_c-1]

def test_up_buttom():
    test_str = 'character'
    print(set_memorize(test_str, 0, len(test_str) - 1)[0])
    print(set_memorize(test_str, 0, len(test_str) - 1)[1])
    test_str = 'aibohphobia'
    print(set_memorize(test_str, 0, len(test_str) - 1)[1])


if __name__ == "__main__":
    # test_up_buttom()
    find_longest_palindrome_bottom_up("aibohphobia")