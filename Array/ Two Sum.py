"""Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target."""

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))