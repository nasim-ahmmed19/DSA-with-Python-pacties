#Armstrong Number 
def check_armstrong(num):
    n=num
    nod=len(str(num))
    result=0
    while n>0:
        ls=n%10
        result=result+(ls**nod)
        n//=10
    return result==num

print(check_armstrong(153))
