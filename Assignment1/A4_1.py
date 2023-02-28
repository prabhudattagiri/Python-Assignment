# 4. Write a python program to compute following series and take input x and n
# I. 1-x2/2! + x3/3!-x4/4!+------+xn/n!
x=int(input("Enter the value of x : "))
n=int(input("Enter the value of n : "))
count,result=1,1
for i in range(2,n+1):
    pow,fact=1,1
    for j in range(1,i+1):
        pow=pow*x
        fact=fact*j
    r=pow/fact
    if count%2==0:
        result=result+r
    else:
        result=result-r
    count=count+1

print("Result of the series is ",result)