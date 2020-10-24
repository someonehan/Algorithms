"""Given a non-negative integers a1, a2, a3, an, where each
represents a point at coordinate (i, ai), n vertical lines


Approach 2 : 2 Pointer Approach

the intuition behind approach is that the area formed between the lines will always
be limited by the height of the shorter line, Further, the farther the lines, the
more will be the area obtained

take two pointers, one at the beginning and one at the end of the array constituting
the length of the lines, Further, we maintain a variable maxarea to store the area
obtained till now, at every step, we find out the area formed between them, update
maxarea and move the pointer pointing to the shorter line torwards the other end by
one step
"""

class Solution:
    def max_area(self, heights : list[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = -1
        while i < j:
            if heights[i] <= heights[j]:
                max_area = max(max_area, heights[i] * heights[j])
                i += 1
            else:
                max_area = max(max_area, heights[i] * heights[j])
                j -= 1
        return max_area