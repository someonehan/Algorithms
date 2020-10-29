"""you are given an integer array nums sorted in ascending order, and an integer target

support that nums is rotated at some pivot unknown to you beforehand
([0, 1, 2, 4, 5, ,6 ,7]) migth before [4, 5, 6, 7, 0, 1, 2]

if target is found in the array return its index, otherwise return -1
"""

class Solution:
    def search(self, nums : list[int], target : int) -> int:
        lo, hi  = 0, len(nums) -1 
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[hi]:
                if target < nums[lo] and target < nums[mid]
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if target > nums[hi] and target > nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return hi