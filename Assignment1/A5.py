# Write a java program compute following series and take a numbers num as input  x-x3/3! + x5/5!-x7/7!+------+xn/n!
# where x=sum of all even digits except 2 and 8 and n= sum of all odd digits except 1 and 3

num=int(input("Enter a Number : "))
x=n=0
# for find value of x and n
while num!=0:
    t=num%10
    if(t%2==0 and t!=2 and t!=8):
        x=x+t
    else:
        if (t!=1 and t!=3):
            n=n+t
    num=num//10

# Calculate the series
result,count=x,1
for i in range(3,n+1,2):
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