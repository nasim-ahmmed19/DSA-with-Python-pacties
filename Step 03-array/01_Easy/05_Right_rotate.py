# Right rotate an array by k steps, where k is non-negative.
def right_rotate(arr,k):
    n=len(arr)
    i=0
    j=n-k-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr
nums = [1,2,3,4,5,6,7]
print(right_rotate(nums,3))