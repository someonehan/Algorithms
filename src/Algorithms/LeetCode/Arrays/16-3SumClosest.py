""" given an array nums of n integers and an integer target, find three
integers in nums such that the sum is closest to target, 
return the sum of the three integers
"""

class Solution:
    def three_sum_closest(self, nums : list[int], target : int) -> int:
        diff = float('inf')
        nums = sorted(nums)

        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else: hi -= 1
            if diff == 0:
                break
        return target - diff
    
