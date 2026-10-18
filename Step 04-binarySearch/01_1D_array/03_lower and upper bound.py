# Lower Bound
def lowerBound(num,target):
    n=len(num)
    low,high=0,n-1
    lb=-1
    while low<=high:
        mid=(low+high)//2
        if num[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb

# Upper Bound
def upperBound(num,target):
    n=len(num)
    low,high=0,n-1
    ub=n
    while low<=high:
        mid=(low+high)//2
        if num[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid++1
    return ub

num=[1,2,2,2,3,3,3,4,4,4,5,5,5,6,7,8,9]
print(lowerBound(num,5)) # Time Complexity: O(log n) space Complexity: O(1)
print(upperBound(num,5)) # Time Complexity: O(log n) space Complexity: O(1)