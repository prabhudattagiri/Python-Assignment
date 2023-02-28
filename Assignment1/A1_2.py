# 1. Write a python program to find following using looping and decision making without function
# II. Sum of all even digits of any number

n=int(input("Enter a Number : "))
sum,num=0,n
while n!=0:
    t=n%10
    if t%2==0:
        sum=sum+t
    n=n//10

print("Sum of all even digits of",num,"is",sum)