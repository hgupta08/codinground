def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring('zxyzxyz'))

#Sliding window problem
#1.we are keep on aading character in set till we find the repeting charatcter
#2.if found remove the instial characher and move ahead
