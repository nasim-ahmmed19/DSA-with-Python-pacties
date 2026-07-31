class freq_map:
    def __init__(self,num):
        n=num
        self.n=n
        self.dict={}
        for i in self.n:
            self.dict[i]=self.dict.get(i,0)+1

    def freqency(self,x):
        count=self.dict.get(x,0)
        print(self.dict)
        print(f'{x} occurs in {count} times')


num=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,4,3,3,2,2,1,1,4,6,7,8,8,9,9]
obj=freq_map(num)
obj.freqency(12)