def largestcontinoussum(nums):

    max_sum=nums[0]
    current_sum=nums[0]

    for i in range(1,len(nums)):

        current_sum=max(current_sum+nums[i],nums[i])
        max_sum = max(current_sum,max_sum)

    return max_sum
print(largestcontinoussum([0, 2, -2, -20, 10]))

#answer 10