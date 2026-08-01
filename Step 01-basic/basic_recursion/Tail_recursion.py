def tail_rec(n:int,m:str):
    if n==4:
        return
    print(m)
    tail_rec(n+1,m)
    

tail_rec(0,'Tail Recursion') #TC=O(N)   SC=O(N)