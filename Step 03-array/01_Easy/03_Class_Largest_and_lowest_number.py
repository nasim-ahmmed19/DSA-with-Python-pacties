class solution: 
    def __init__(self,num): 
        self.num=num
        self.n=len(num)
    
    def largest(self,position:int): 
        if position<1 or position>3 or self.n<position: 
            return None
        largest=float('-inf')
        second_largest=float('-inf')
        thired_largest=float('-inf')
        for i in range(0,self.n): 
            if self.num[i]>largest: 
                thired_largest=second_largest
                second_largest=largest
                largest=self.num[i]
            elif self.num[i]>second_largest and self.num[i]!=largest: 
                thired_largest=second_largest
                second_largest=self.num[i]
            elif self.num[i]>thired_largest and self.num[i]!=largest and self.num[i]!=second_largest: 
                thired_largest=self.num[i]
        if position==1: 
            return largest
        if position==2: 
            return second_largest if second_largest != float("-inf") else None
        if position==3: 
            return thired_largest if thired_largest != float("-inf") else None

    def lowest(self,position:int): 
        if position<1 or position>3 or self.n<position: 
            return None
        lowest=float('inf')
        second_lowest=float('inf')
        thired_lowest=float('inf')
        for i in range(0,self.n): 
            if self.num[i]<lowest: 
                thired_lowest=second_lowest
                second_lowest=lowest
                lowest=self.num[i]
            elif self.num[i]<second_lowest and self.num[i] !=lowest: 
                thired_lowest=second_lowest
                second_lowest=self.num[i]
            elif self.num[i]<thired_lowest and self.num[i]!=lowest and self.num[i]!=second_lowest: 
                thired_lowest=self.num[i]
        if position==1: 
            return lowest
        if position ==2: 
            return second_lowest if second_lowest != float("inf") else None 
        if position==3: 
            return thired_lowest if thired_lowest != float("inf") else None

num=[33,42,-3,-87,89,90,92,0,32,99,-9,1,2]

obj=solution(num)
print('Largest number in the array: ',obj.largest(1))
print('Second largest number in the array: ',obj.largest(2))
print('Third largest number in the array: ',obj.largest(3))
print()
print('Lowest number in the array is: ',obj.lowest(1))
print('Second Lowest number in the array is: ',obj.lowest(2))
print('Third Lowest number in the array is: ',obj.lowest(3))

