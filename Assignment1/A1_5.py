# V. Difference between average of all even digits except divisible  by 4 and avearge of all odd digits except divisble by 3

num=n=int(input("Enter a Number : "))
se,so,ce,co=0,0,0,0

while n!=0:
    t=n%10
    if (t%2==0 and t%4!=0):
        se=se+t
        ce=ce+1
    if (t%2!=0 and t%3!=0):
        so=so+t
        co=co+1
    n=n//10
    
ae=se/ce
ao=so/co
diff=ae-ao
print("Difference between average of all even digits except divisible by 4 and avearge of all odd digits except divisble by 3 of number ",num,"is ",diff)