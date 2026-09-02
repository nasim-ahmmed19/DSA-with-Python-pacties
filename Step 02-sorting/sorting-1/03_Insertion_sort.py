# Insertion Sort Algorithm Implementation in Python
# Ascending order

def asc_insertion_sort(num):
    n=len(num)
    for i in range(1,n):
        key=num[i]
        j=i-1
        while j>=0 and num[j]>key:
            num[j+1]=num[j]
            j-=1
        num[j+1]=key
    return num

num=[64, 34, 25, 12, 22, 11, 90]
asc_insertion_sort(num)
print("Sorted array in ascending order is:", num)

# Descending order
def desc_insertion_sort(num):
    n=len(num)
    for i in range(1,n):
        key=num[i]
        j=i-1
        while j>=0 and num[j]<key:
            num[j+1]=num[j]
            j-=1

        num[j+1]=key
    return num
desc_insertion_sort(num)
print("Sorted array in descending order is:", num)