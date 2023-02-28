# 2. Write a python program to find sum of product of corresponding digits of two 
# any digit number Such as n=1234 m=7896 output=6*4+9*3+8*2+7*1

n1=n=int(input("Enter first Number :"))
m1=m=int(input("Enter second Number :"))
sum=0
while (n!=0 or m!=0):
    t1=n%10
    t2=m%10
    sum=sum+(t1*t2)
    n=n//10
    m=m//10

print("Sum of product of corresponding digit of ",n1,"and",m1,"is",sum)