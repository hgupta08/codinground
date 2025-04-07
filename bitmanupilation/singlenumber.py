# You are given a non-empty array of integers nums. Every integer appears twice except for one.
#
# Return the integer that appears only once.
def singlenumber(n):

    d=set()
    for i in n:
        if i in d:
            d.remove(i)
        else:
            d.add(i)
    return list(d)[0]


def single(nums):
    res = 0
    for num in nums:
        res = num ^ res
    return res


nums = [3,2,3]
print(singlenumber(nums))

#print(single(nums))