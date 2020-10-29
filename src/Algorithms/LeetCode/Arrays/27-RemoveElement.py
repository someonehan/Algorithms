""" given an array nums and a value val, remove all instances of that value in place 
and return the new length
do not allocate extra spce for another array, you must do this by nodifying the input
array in-place with O(1) extra memory
the order of elements can be changed
"""

class Solution:
    def removeElement(self, nums : list[int], val : int) -> int:
        i = 0 
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def removeElement2(self, nums : list[int], val : int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == val:
                nums[i] = nums[i + 1]
                j -= 1
            else:
                i += 1
        return i