# Python3 program to count frequencies of array items
def countFreq(arr, n):
    mp = {}

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
            print(mp)
        else:

            mp[arr[i]] = 1

    # Traverse through array elements and
    # count frequencies

    # To prelements according to first
    # occurrence, traverse array one more time
    # prfrequencies of elements and mark
    # frequencies as -1 so that same element
    # is not printed multiple times.
    for key, value in mp.items():
        print(key, value)


# Driver code

arr = [10, 10, 20, 10, 10, 20, 5, 20]
n = len(arr)
countFreq(arr, n)

# This code is contributed by shubhamsingh10