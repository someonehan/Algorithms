"""
find the max totle value of subarray from the array

"""

# method 1
# split the array, the maximun subarray is in the left array right array and cross the left and right array

import sys

def Find_maxarray_crossarray(A,low,mid,high):
    left_large = -sys.maxsize
    left_sum = 0
    left_max = mid

    for i in range(mid -1,low-1,-1):
        left_sum += A[i]
        if left_sum > left_large:
            left_large = left_sum
            left_max = i

    right_large = -sys.maxsize
    right_sum = 0
    right_max = mid
    for i in range(mid, high + 1):
        right_sum += A[i]
        if right_sum > right_large:
            right_large = right_sum
            right_max = i
    return left_max,right_max,left_large + right_large

def Maximum_subarray(A,low,high):
    if low == high:
        return low,high,A[low]

    else:
        mid = (low + high) // 2
        left_values  = Maximum_subarray(A,low,mid)
        right_values = Maximum_subarray(A,mid + 1, high)

        cross_values = Find_maxarray_crossarray(A, low, mid, high)
        if cross_values[2] >= left_values[2] and cross_values[2] >= right_values[2]:
            return cross_values
        elif left_values[2] >= right_values[2] and left_values[2] >= right_values[2]:
            return left_values
        else: 
            return right_values

def test_Maximum_subarray():
    l = [-1,-2,3,24,2,-3,-3]
    print(l)
    max_left,max_right,max_sum = Maximum_subarray(l,0,len(l) -1)
    print("the maximum array is {0} and sum is {1}".format([item for item in l[max_left:max_right + 1]],max_sum))


# and there is another way find out the max subarray

def Find_maxsubarray(A):
    largest = -sys.maxsize    
    current_sum = 0

    for i in range(0,len(A)):
        current_sum += A[i]        
        if current_sum > largest:largest = current_sum
        if current_sum < 0:current_sum = 0

    return largest

def test_Find_maxsubarray():
    l = [-1,-2,3,24,2,-3,-3]
    
    max_sum = Find_maxsubarray(l)

    print(max_sum)


if __name__ == "__main__":
    test_Maximum_subarray()
    test_Find_maxsubarray()

