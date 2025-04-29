import random


# Function to perform quick select
def quick_select(arr, k):
    # Randomly select a pivot
    pivot = random.choice(arr)

    # For elements greater than the pivot
    leftArr = [x for x in arr if x > pivot]

    # For elements equal to the pivot
    midArr = [x for x in arr if x == pivot]

    # For elements less than the pivot
    rightArr = [x for x in arr if x < pivot]

    # Recursive selection
    if k <= len(leftArr):
        return quick_select(leftArr, k)
    if len(leftArr) + len(midArr) < k:
        return quick_select(rightArr, k - len(leftArr) - len(midArr))

    # Return pivot as the k-th largest
    return pivot


# Wrapper function to find the k-th largest
def kth_largest(arr, k):
    return quick_select(arr, k)


if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19]
    k = 2
    print(kth_largest(arr, k))
