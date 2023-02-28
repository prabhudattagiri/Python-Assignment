# 1. Write a python program to find following using looping and decision making without function
# IV. Sum of all prime digits

n=int(input("Enter a Number : "))
sum,num=0,n
while n!=0:
    prime=False
    t=n%10
    if t!=1: # bcs 1 is not prime number
        prime=True
    for i in range(2,t):
        if t%i==0:
            prime = False
    if (prime):
        sum=sum+t
    n=n//10

print("Sum of all prime digits of",num,"is",sum)