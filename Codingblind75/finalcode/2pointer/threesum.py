# python program to find triplets in a given
# array whose sum is zero

# function to print triplets with 0 sum
def findTriplets(arr, n):
    found = False

    # sort array elements
    arr.sort()
    res=[]

    for i in range(len(arr)):

        # initialize left and right

        l = i
        r = n - 1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(res)
                curr=[x, arr[l], arr[r]]
                if curr not in res:
                    res.append([x, arr[l], arr[r]])
                l += 1
                r -= 1
                found = True
            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1

    return res
    # if (found == False):
    #     print(" No Triplet Found")

    # Driven source


arr = [-1,0,1,2,-1,-4]
n = len(arr)
print(findTriplets(arr, n))

# This code is contributed by Smitha Dinesh Semwal