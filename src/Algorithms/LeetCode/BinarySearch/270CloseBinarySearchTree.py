# Given a non-empty binary search tree and a target value, 
# find the value in the BST that is closest to the target.

# Note:

#     Given target value is a floating point.
#     You are guaranteed to have only one unique value in the BST that is closest to the target.

class Node:
    __slots__ = 'left', 'right', 'parent', 'value'

class Solution:
    def CloseBinarySearch(self, node, target):
        child = node
        while child:
            if child.value > target:
                child = child.left
            elif child.value < target:
                child = child.right
            else:return child.value

        return min(child.value, child.parent.value, key=lambda x: abs(x.value - target))
        

        
        
