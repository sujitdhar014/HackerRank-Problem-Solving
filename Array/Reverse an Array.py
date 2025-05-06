 # Return the reversed array
def reverse_array(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums 

nums = [1, 2, 3, 4]
print(reverse_array(nums))