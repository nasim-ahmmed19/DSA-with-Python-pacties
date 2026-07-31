class freq_map:
    def __init__(self,num):
        n=num
        self.n=n
        self.dict={}

    def frequency(self,x):
        for i in self.n:
            if i in self.dict:
                self.dict[i]+=1
            else:
                self.dict[i]=1
        print(self.dict)
        print(f'{x} in the list :{self.dict[x]} time')

num=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,4,3,3,2,2,1,1,4,6,7,8,8,9,9]
obj=freq_map(num)
obj.frequency(3) #TC= O(N) .. SC=O(N)
