# Merge sort implementation in Python
# Ascending order

def asc_merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)

    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i<n:
        result.extend(left[i:])

    if j<m:
        result.extend(right[j:])
    return result

def merge_sort(num):
    if len(num)<=1:
        return num
    mid=len(num)//2
    left_arr=num[:mid]
    right_arr=num[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return asc_merge_array(left,right)

num=[64, 34, 25, 12, 22, 11, 90]
sorted_array=merge_sort(num)
print("Sorted array in ascending order is:", sorted_array) # TC: O(nlogn) SC: O(n)


# Descending order
def desc_merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)

    while i<n and j<m:
        if left[i]>=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i<n:
        result.extend(left[i:])

    if j<m:
        result.extend(right[j:])
    return result

def merge_sort(num):
    if len(num)<=1:
        return num
    mid=len(num)//2
    left_arr=num[:mid]
    right_arr=num[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return desc_merge_array(left,right)

desc_sorted_array=merge_sort(num)
print("Sorted array in descending order is:", desc_sorted_array) # TC: O(nlogn) SC: O(n)