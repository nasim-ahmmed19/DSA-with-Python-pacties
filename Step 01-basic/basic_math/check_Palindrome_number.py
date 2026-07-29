#Create Function to check Palindrome number
def check_palindrome(num):
    n=num
    result=0
    while n>0:
        ls=n%10
        result=(result*10) + ls
        n//=10
    return result==num

print(check_palindrome(552))

        
        