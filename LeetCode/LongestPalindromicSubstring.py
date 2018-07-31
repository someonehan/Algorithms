
"""
giving a string s, find the longest palindromic substring of s
"""

def findLongestPalindromicAtMid(s, left, mid, right):
    '''

    :return:
    '''



def findLongestPalindromic(s, left, right):
    '''

    :return:
    '''
    if right == left:
        return 0, s[left]
    if right - left == 1 and s[left] == s[right]:
        return len(s[left:right]), s[left:right]
    mid = (left + right) // 2
    left_len, left_str = findLongestPalindromic(s, left, mid)
    mid_len, mid_str = findLongestPalindromicAtMid(s, left, mid, right)
    right_len, right_str = findLongestPalindromic(s, mid + 1, right)

    if left_len > mid_len and left_len > right_len:
        return left_len, left_str
    elif mid_len > left_len and mid_len > right_len:
        return mid_len, mid_str
    else:
        return right_len, right_str

def test_findLongestPalindromic():
    s = 'abba'
    print(findLongestPalindromic(s, 0, 3))

if __name__ == "__main__":
    test_findLongestPalindromic()