# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2

# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.


class Solution:
    def Sqrt(self, x):
        if x <= 0: return 0
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if (x / mid) == mid:
                return mid
            elif (x / mid) < mid:
                right = mid - 1
            else: left = mid + 1

        return right

if __name__ == "__main__":
    s = Solution()
    print(s.Sqrt(8))

