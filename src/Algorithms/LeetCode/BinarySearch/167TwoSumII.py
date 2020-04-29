# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, 
# where index1 must be less than index2.

# Note:

#     Your returned answers (both index1 and index2) are not zero-based.
#     You may assume that each input would have exactly one solution and you may not use the same element twice.

# Example:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

class Solution:
    def TwoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] > target:
                right = right - 1
            else:
                left = left + 1

    def TwoSum2(self, nums, target):

        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]] + 1, i+1]
            else:
                x = target - nums[i]
                d[x] = i 

if __name__ == "__main__":
    s = Solution()
    print(s.TwoSum2([2, 7, 11, 15], 9))        