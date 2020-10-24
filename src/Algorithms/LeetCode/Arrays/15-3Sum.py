""" given a array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0 ? find all unique triple in the array which givens
the sum of zero
"""

class Solution:
    def threeSum(self, nums : list[int]) -> list[int]:
        ans = set()
        nums = sorted(nums)        
        for index in range(len(nums) - 1)
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            i = index + 1
            j = len(nums) - 1
            while i < j:
                s = nums[index] + nums[i] + nums[j]
                if s == 0:
                    ans.add((nums[index], nums[i], nums[j]))
                elif s > 0:
                    j = j - 1
                else:
                    i = i + 1
        return list(ans)