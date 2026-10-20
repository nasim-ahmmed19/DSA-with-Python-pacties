class Solution:
    def __init__(self, nums: list[int], target: int) -> list[int]:
        self.nums=nums
        self.target=target
    def lowerBound(self):
        n=len(self.nums)
        low,high=0,n-1
        lb=n
        while low<=high:
            mid=(low+high)//2
            if self.nums[mid]>=self.target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    def upperBound(self):
        n=len(self.nums)
        low,high=0,n-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            if self.nums[mid]>self.target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub
    def searchRange(self):
        lb=self.lowerBound()
        ub=self.upperBound()
        if lb==len(self.nums) or self.nums[lb]!=self.target:
            return [-1,-1]
        return [lb,ub-1]    
nums=[5,7,7,8,8,10]
obj=Solution(nums,6)
print([obj.searchRange()])