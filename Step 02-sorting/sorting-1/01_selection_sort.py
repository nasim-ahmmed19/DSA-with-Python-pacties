# Selection Sort Algorithm Implementation in Python
# Ascending Order

def selection_sort(num):
    n=len(num)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]

num=[2,4,5,6,7,1,3,4,2,1,8,9,10]
selection_sort(num)
print("Sorted array in ascending order:", num)

# Descending Order
def selection_sort_descending(num):
    n=len(num)
    for i in range(0,n):
        max_index=i
        for j in range(i+1,n):
            if num[j]>num[max_index]:
                max_index=j
        num[i],num[max_index]=num[max_index],num[i]

num=[2,4,5,6,7,1,3,4,2,1,8,9,10]
selection_sort_descending(num)
print("Sorted array in descending order:", num)