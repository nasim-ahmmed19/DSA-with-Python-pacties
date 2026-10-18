def binarySearch(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
num=[1,2,2,2,3,3,3,4,4,4,5,5,5,6,7,8,9]
target=5
print(binarySearch(num,target))
