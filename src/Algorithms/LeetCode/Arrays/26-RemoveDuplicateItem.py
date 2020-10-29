"""given a sorted array numbs, remove the duplicates in-place such
that each elements appears only once and return the new length
do not allocate extra space for another array, 
must do this by modifying the input array in-place with O(1) extra memory
"""

# Approach 1 : two Pointers
# since the array is sorted, we can keep two pointers i and j, where i is the slow-runner
# while j is the fast-runner, as long as nums[i] == nums[j], we increment j to skip the 
# duplicate

# when we encounter nums[j] != nums[i]


class Solution:
    def removeDuplicates(self, nums : list[int]) -> int:
        if len(nums) == 0 : return 0
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
