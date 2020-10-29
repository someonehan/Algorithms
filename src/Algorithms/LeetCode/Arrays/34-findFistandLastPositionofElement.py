""" given an array of integers nums sorted in ascending order, first the starting and
the ending position of a given target value.

if target is not found in the array return [-1, -1]

Example:
input nums [1, 7, 7, 8, 8, 10] target = 8
return [3, 4]
Example:
input nums [5, 7, 7, 8, 8, 10] target = 6
return [-1, -1]
"""

class Solution:
    def flPosition1(self, nums : list[int], target : int) -> list[int]:
        for index, elem in enumerate(nums):
            left_found = False
            if not left_found and elem == target:
                lo = index
                left_found = True
            if left_found:
                if elem > target:
                    hi = index - 1
                    return [lo, hi]
        return [-1, -1]

    def find_insert_pos(self, nums : list[int], target : int, left : bool) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid] or (left ):
                lo = mid
            else:
                hi = mid


