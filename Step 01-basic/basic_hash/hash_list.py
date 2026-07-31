num=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,4,3,3,2,2,1,1,4,6,7,8,8,9,9]
m=[2,3,4,5,6] 

# Find how many times each element of m occurs inside num.
class hash_lsit:
    def __init__(self,num,m):
        n=num
        self.n=n
        self.m=m
        self.hash_ls=[0]*11

    def counter(self):
        for i in self.n:
            self.hash_ls[i]+=1

        for j in self.m:
            if j<0 or j>10:
                print(f'{j} occurs in list :{0} times')
            else:
                print(f'{j} occurs in list :{self.hash_ls[j]} times')


obj=hash_lsit(num,m)
obj.counter()

