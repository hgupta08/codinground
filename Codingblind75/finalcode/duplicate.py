# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
# Example 1:
#
# Input: nums = [1, 2, 3, 3]
#
# Output: true

def findduplicate(nums):

    ht = {}

    for i in range(0,len(nums)):

        print(ht)

        if nums[i] in ht:
            return True
        else:
            ht[nums[i]] = i


    return False

print(findduplicate([5, 6, 7, 8]))
