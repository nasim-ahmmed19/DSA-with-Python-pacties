class Solution:
    def lowerBound(self,arr,target):
        n=len(arr)
        low,high=0,n-1
        lb=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    
    def upperBound(self,arr,target):
        n=len(arr)
        low,high=0,n-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub
    def countFreq(self, arr, target):
        lb=self.lowerBound(arr,target)
        ub=self.upperBound(arr,target)
        if lb==len(arr) or arr[lb]!=target:
            return 0
        return ub-lb
nums=[5,7,7,8,8,10]
obj=Solution()
print(obj.countFreq(nums,10))