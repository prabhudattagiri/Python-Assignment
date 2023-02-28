# III. 1+x2/2! + x4/4!+x6/6!+------+xn/n!
x=int(input("Enter value of x : "))
n=int(input("Enter value of n : "))
result=1
for i in range(2,n+1,2):
    pow=fact=1
    for j in range(1,i+1):
        pow=pow*x
        fact=fact*j
    r=pow/fact
    result=result+r

print("Result of the series is ",result)