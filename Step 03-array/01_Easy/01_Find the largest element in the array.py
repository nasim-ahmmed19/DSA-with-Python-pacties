# Find the largest element in the array
def find_largest_element(arr):
    largest=float('-inf')
    for i in range(0,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest

num=[2,3,4,5,6,7,8,9]
print("The largest element in the array is:",find_largest_element(num))

def find_largest_element(arr):
    largest=float('-inf')
    for i in arr:
        largest=max(largest,i)
    return largest
print("The largest element in the array is:",find_largest_element(num)) #TC O(n) and SC O(1)