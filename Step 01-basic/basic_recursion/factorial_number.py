def fact_num(n):
    if n==0 or n==1:
        return 1
    return n * fact_num(n-1)

print(fact_num(5)) #TC=O(N)   SC=O(N)