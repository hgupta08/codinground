def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
    """
    sum = 0
    n = len(nums)

    total = (n + 1) * (n + 2) / 2
    for i in range(0, len(nums)):
        sum = sum + nums[i]

    missing_no = total - sum
    return missing_no

nums = [1, 2, 3,4,5,7]
a = missingNumber(nums)
print(a)


# Python program to find the missing number

def missingNumber(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0

    # XOR all array elements
    for num in arr:
        xor2 ^= num

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor1 ^= i

    # Missing number is the XOR of xor1 and xor2
    return xor1 ^ xor2


if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    res = missingNumber(arr)
    print(res)
