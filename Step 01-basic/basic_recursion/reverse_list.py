def reverse_list(lst,l,r):
    if l>=r:
        return
    lst[l],lst[r]=lst[r],lst[l]
    reverse_list(lst,l+1,r-1)

num=[1,2,3,4,5]
reverse_list(num,0,len(num)-1)
print(num) #TC=O(N)   SC=O(N)