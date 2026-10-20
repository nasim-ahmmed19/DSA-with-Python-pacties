def ceil_floor(num,x):
    n=len(num)  
    low,high=0,n-1
    res=[-1,-1]
    while low<=high:
        mid=(low+high)//2
        if num[mid]>=x:
            res[1]=num[mid]
            high=mid-1
        if num[mid]<=x:
            res[0]=num[mid]
            low=mid+1
    return res
num=[3,4,4,7,8,10]
x=2
print(ceil_floor(num,x))
x=8
print(ceil_floor(num,x))
