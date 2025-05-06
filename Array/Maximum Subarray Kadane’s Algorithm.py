# Maximum Subarray (Kadane’s Algorithm)
"""Problem:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.

"""
def max_sub_array(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))