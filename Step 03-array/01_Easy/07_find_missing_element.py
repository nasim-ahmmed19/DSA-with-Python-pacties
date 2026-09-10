def find_missing(num):
    n=len(num)
    dic={}
    for i in  range(0,n+1):
        dic[i]=0
    for j in num:
        dic[j]=1
    for k,v in dic.items():
        if v==0:
            return k

n=[3,0,1]
print(find_missing(n)) # TC O(n) SC O(n)

def find_missing_2(num):
    n=len(num)
    total_sum=(n*(n+1))//2
    sum_of_array=sum(num)
    return total_sum-sum_of_array

print(find_missing_2(n)) # TC O(n) SC O(1)