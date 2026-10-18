def re_bs(num,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if num[mid]==target:
        return mid
    elif num[mid]<target:
        return re_bs(num,target,mid+1,high)
    else:
        return re_bs(num,target,low,mid-1)
num=[1,2,2,2,3,3,3,4,4,4,5,5,5,6,7,8,9]
target=5    
print(re_bs(num,target,0,len(num)-1)) # Time Complexity: O(log n) space Complexity: O(log n)
