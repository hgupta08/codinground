

def majorityelement(nums):

    me=None
    count =0
    for i in range(len(nums)):
        if count==0:
            me=nums[i]
        if me==nums[i]:
            count=count+1

        else:
            count=count-1
    count = 0
    for num in nums:
        if num == me:
            count += 1

    # If count is greater than n / 2, return the candidate; otherwise, return -1
    if count > len(nums) // 2:
        return me
    else:
        return -1

print(majorityelement([2,2,2,1,0]))