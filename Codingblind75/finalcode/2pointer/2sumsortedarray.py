def twoSum(numbers, target: int):
    l, r = 0, len(numbers) - 1

    a=[]

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            a.append([l+1,r+1])
    return a

print(twoSum([1,2,1,2],3))