# 1. Write a python program to find following using looping and decision making without function
# I. Sum of all digits of any numbers

n=int(input("Enter a Number :"))
sum,num=0,n
while n!=0:
    sum=sum+(n%10)
    n=n//10

print("Sum of all digits of",num,"is",sum)