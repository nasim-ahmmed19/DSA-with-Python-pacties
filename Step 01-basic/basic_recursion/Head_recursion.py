def head_rec(n:int,m:str):
    if n==0:
        return
    head_rec(n-1,m)
    print(m)

head_rec(4,'Head Recursion') #TC=O(N)   SC=O(N)