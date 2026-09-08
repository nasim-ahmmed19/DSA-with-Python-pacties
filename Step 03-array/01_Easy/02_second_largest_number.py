# Find the second largest element in the array
def find_second_largest_element(arr):
    largest=float('-inf')
    second_largest=float('-inf')
    for i in range(0,len(arr)):
        largest=max(largest,arr[i])
    for j in range(0,len(arr)):
        if arr[j]>second_largest and arr[j]!=largest:
            second_largest=arr[j]
    return second_largest

num=[2,3,4,5,6,7,8,9]
print("The second largest element in the array is:",find_second_largest_element(num)) #TC O(n) and SC O(1)