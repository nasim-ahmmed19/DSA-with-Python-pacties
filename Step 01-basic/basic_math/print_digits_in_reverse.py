# Function to print digits in reverse
def reverse(num):
    n=num
    while n>0:
        last_digit=n%10
        print(last_digit)
        n=n//10

reverse(5883)