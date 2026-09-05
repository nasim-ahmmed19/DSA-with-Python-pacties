# Quick sort implementation in Python
# Ascending order

def asc_partition(arr,low,high):
    pivot=arr[low]
    i,j=low,high

    while i<j:
        while i<=high-1 and arr[i]<=pivot:
            i+=1
        while j>=low+1 and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

num=[64, 34, 25, 12, 22, 11, 90]
low=0
high=len(num)-1

def asc_quick_sort(arr,low,high):
    if low<high:
        pivot_index=asc_partition(arr,low,high)
        asc_quick_sort(arr,low,pivot_index-1)
        asc_quick_sort(arr,pivot_index+1,high)

asc_quick_sort(num,low,high)
print("Sorted array in ascending order is:", num) # TC: O(nlogn) SC: O(logn)

# Descending order
def desc_partition(arr,low,high):
    pivot=arr[low]
    i,j=low,high
    while i<j:
        while i<=high-1 and arr[i]>=pivot:
            i+=1
        while j>=low+1 and arr[j]<pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def desc_quick_sort(arr,low,high):
    if low<high:
        pivot_index=desc_partition(arr,low,high)
        desc_quick_sort(arr,low,pivot_index-1)
        desc_quick_sort(arr,pivot_index+1,high)

desc_quick_sort(num,low,high)
print("Sorted array in descending order is:", num) # TC: O(nlogn)   