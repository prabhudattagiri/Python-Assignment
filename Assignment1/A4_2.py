# II. x-x3/3! + x5/5!-x7/7!+------+xn/n!
x=int(input("Enter value of x : "))
n=int(input("Enter value of n : "))
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