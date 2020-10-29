""" given an array nums of n integers and an integer target, are there
elements a, b, c and d in nums such that a + b + c + d = target
find all unique quadruplets in the array which gives the sum of the target
"""

class Solution:
    def fourSum(self, nums : list[int], target : int) -> list[list[int]]:
        def kSum(nums : list[int], target : int, k : int) -> list[list[int]]:
            res = []
            if nums[0] > target or nums[0] * k > target or nums[-1] * k < target:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i -1] != nums[i]:
                    for _, s in enumerate(kSum(nums[i : -1]), target - nums[i], k - 1):
                        res.append(nums[i] + s)
            return res

        def twoSum(nums : list[int], target : int) -> list[list[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                sum_ = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi += 1
                else:
                    res.append([nums[lo], nums[hi]])
            return res

        nums = sorted(nums)
        return kSum(nums, target, 4)