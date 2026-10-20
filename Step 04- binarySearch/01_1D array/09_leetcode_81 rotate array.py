def rotateArray(num,target):
    n=len(num)
    low,high=0,n-1
    res=False
    while low<=high:
        mid=(low+high)//2
        if num[mid]==target:
            res=True
            return res
        elif num[low]<=num[mid]:
            if num[low]<=target<num[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if num[mid]<target<=num[high]:
                low=mid+1
            else:
                high=mid-1
    return res
num=[2,5,6,0,0,1,2]
target=8
print(rotateArray(num,target))