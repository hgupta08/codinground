def twosum(arr,target):


    dm={}
    count = 0

    for i in range(0,len(arr)):
        val=target-arr[i]
        if val in dm:
            print(f"Sum of {arr[i]} and {val} at  index {i} and {arr.index(val)}")
            count=count+1
        else:
            dm[arr[i]]=i
    return count






a=twosum(arr=[-1, 5, 7, 1], target=6)

if (a==0):
    print("No element with sum")
