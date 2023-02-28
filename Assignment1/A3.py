# 3. Write a python program to find sum of product of corresponding even digits 
# of first any digit number and corresponding odd digit of any digit number 
# Such as n=1234 m=4567 output=4*7+2*5
n1=n=int(input("Enter first Number : "))
m1=m=int(input("Enter second Number : "))
sum=0
while (n!=0 or m!=0):
    t1=n%10
    t2=m%10
    if (t1%2==0 and t2%2!=0):
        sum=sum+(t1*t2)
    n=n//10
    m=m//10

print("Sum of product of corresponding even digits of",n1,"and corresponding odd digit of",m1," is ",sum)
