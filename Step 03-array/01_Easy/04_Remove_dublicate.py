# Remove Duplicates from Sorted Array

def remove_dublicates(arr):
    n=len(arr)
    if n==1: 
        return 1
    i=0
    j=1
    while j<n:
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
        j+=1
    return i+1
num=[1,1,2,2,4,5,5,6]
print("The length of the array after removing duplicates is:",remove_dublicates(num)) #TC O(n) and SC O(1)
print("The array after removing duplicates is:",num[:remove_dublicates(num)])
    