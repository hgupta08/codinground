\def maxArea(heights):
    l, r = 0, len(heights) - 1
    res = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return res

# You are given an integer array heights where heights[i] represents the height of the
# i
# t
# h
# i
# th
#   bar.
#
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.
#
# Example 1:

# Input: height = [1,7,2,5,4,7,3,6]
#
# Output: 36