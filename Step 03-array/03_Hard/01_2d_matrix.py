num=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

class matrix:
    def __init__(self,num):
        self.num=num
        self.row=len(num)
        self.col=len(num[0])
    def upper_triangle(self):
        for i in range(0,self.row):
            for j in range(0,self.col):
                if j>=i:
                    print(num[i][j],end='  ')
                else:
                    print('*',end='  ')
            print()

    def lower_triangle(self): 
        for i in range(0,self.row): 
            for j in range(0,self.col):
                if i>=j: 
                    print(num[i][j],end='  ')
                else:
                    print('*',end='  ')
            print()

    def diagonal_1(self):
        for i in range(0,self.row):
            for j in range(0,self.col):
                if i==j:
                    print(num[i][j],end='  ')
                else:
                    print('*',end='  ')
            print()

    def diagonal_2(self):
        for i in range(0,self.row):  
            for j in range(0,self.col): 
                if i+j==2: 
                    print(num[i][j],end='  ')
                else:
                    print('*',end='  ')
            print()

    def transope_matrix(self):
        result=[[0]*self.row for _ in range(self.col)]
        for i in range(0,self.row): 
            for j in range(0,self.col): 
                result[j][i]=num[i][j]
        print(result)
obj=matrix(num)
#obj.upper_triangle()
#obj.lower_triangle()
#obj.diagonal_1()
#obj.diagonal_2()
obj.transope_matrix()