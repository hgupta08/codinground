# Python3 program to print subarray with sum as given sum
# Function to print subarray with sum as given sum

def subArraySum(arr, n, Sum):
    # create an empty map
    Map = {}

    # Maintains sum of elements so far
    curr_sum = 0
    found=0

    for i in range(0, n):

        #print(Map)

        # add current element to curr_sum
        curr_sum = curr_sum + arr[i]

        # if curr_sum is equal to target sum
        # we found a subarray starting from index 0
        # and ending at index i
        if curr_sum == Sum:
            found=found+1
            print("Sum found between indexes 0 to", i)


            # If curr_sum - sum already exists in map
        # we have found a subarray with target sum
        if (curr_sum - Sum) in Map:
            #print(Map)
            #print("in this")

            print("Sum found between in 5hi indexes", Map[curr_sum - Sum] + 1, "to", i)


        Map[curr_sum] = i

        # If we reach here, then no subarray exists
    print("No subarray with given sum exists")

if __name__ == "__main__":
    arr = [0, 1, 2, 20, 10]
    n = len(arr)
    Sum = 3

    subArraySum(arr, n, Sum)

   # pairArray(arr,Sum)

