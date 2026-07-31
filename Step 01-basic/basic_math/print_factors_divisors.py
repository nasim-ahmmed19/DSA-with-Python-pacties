from math import sqrt
class fact_div():
    def __init__(self,num):
        n=num
        self.n=n
        self.result=[]

    def divisors(self):
        for i in range(1,int(sqrt(self.n))+1):
            if self.n%i==0:
                self.result.append(i)
                if self.n//i !=i:
                    self.result.append(self.n//i)
        self.result.sort()
        return self.result

obj=fact_div(25)
print(obj.divisors()) # TC=O(sqrt(N))+O(K log k) SC=O(K)
