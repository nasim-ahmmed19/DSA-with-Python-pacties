# Bubble sort algorithm implementation in Python
# Ascending order

def bubble_sort(num): # TC: O(n^2) SC: O(1)
    n=len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]

num=[64, 34, 25, 12, 22, 11, 90]
bubble_sort(num)
print("Sorted array in ascending order is:", num) 

# Descending order
def bubble_sort_descending(num):  # TC: O(n^2) SC: O(1)
    n=len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]<num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]


bubble_sort_descending(num)
print("Sorted array in descending order is:", num) 

# Best case time complexity: O(n)
def bubble_sort_best_case(num): # TC: O(n^2) SC: O(1)
    n=len(num)
    for i in range(n-2,-1,-1):
        swapped=False
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
                swapped=True
        if not swapped:
            break

num=[11, 12, 22, 25, 34, 64, 90]
bubble_sort_best_case(num)
print("Sorted array in best case is:", num)
