# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
# nums = [2,7,11,15]
# target = 9
# print(two_sum(nums,target)) # TC O(n^2) SC O(1)

# def two_sum(nums,target): # TC O(n^2) SC O(1)
#     i=0
#     j=i+1
#     n=len(nums)
#     while j<n:
#         if nums[i]+nums[j]==target:
#             return [i,j]
#         j+=1
#         if j==n:
#             i+=1
#             j=i+1

def two_sum(nums,target): #TC O(n) SC O(n)
    hashmap={}
    for i in range(0,len(nums)):
        remaining=target-nums[i]
        if remaining in hashmap:
            return [hashmap[remaining],i]
        hashmap[nums[i]]=i

nums = [3,2,4]
target = 6
print(two_sum(nums,target)) 