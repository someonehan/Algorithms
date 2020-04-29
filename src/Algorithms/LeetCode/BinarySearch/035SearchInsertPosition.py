# Given a sorted array and a target value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2

# Example 2:

# Input: [1,3,5,6], 2
# Output: 1

# Example 3:

# Input: [1,3,5,6], 7
# Output: 4

# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def insertPosition(self, nums, target):
        if len(nums) < 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:# this is the point
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else: right = mid - 1

        return left
if __name__ == "__main__":
    s = Solution()
    print(s.insertPosition([1,3,5,6], 0))



