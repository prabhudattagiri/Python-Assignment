# IV. x-x3/3! + x5/5!-x7/7!+x11/11!------+xn/n!
x=int(input("Enter the value of x : "))
n=int(input("Enter the value of n : "))
result,count=x,1
for i in range(3,n+1,2):
    prime=True
    pow=fact=1
    # Check n is prime or not
    for j in range(2,i):
        if (i%j==0):
            prime=False
    # find pow & fact (if Prime)
    if prime:
        for j in range(1,i+1):
            pow=pow*x
            fact=fact*j
        count=count+1
    r=pow/fact
    if(count%2==0):
        result=result+r
    else:
        result=result-r

print("Result of the series is ",result)