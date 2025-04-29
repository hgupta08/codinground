# Python program to find the most frequent element in an array.

# Function to find the most
# frequent element in an array.
def mostFreqEle(arr):
    n = len(arr)

    # Insert all elements in hash map.
    freq = {}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
        # freq[arr[i]] = freq.get(arr[i], 0) + 1
    print(freq)

    # find the max frequency
    maxCnt, res = 0, -1
    for val, cnt in freq.items():
        print("val",val)
        print("cnt",cnt)
        print("maxcount",maxCnt)
        print("res",res)



        if maxCnt < cnt or (cnt == maxCnt and val > res):
            res = val
            maxCnt = cnt

    return res


if __name__ == "__main__":
    arr = [40, 50, 30, 40, 50, 30, 30]
    print(mostFreqEle(arr))


