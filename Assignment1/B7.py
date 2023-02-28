# Write a python program to find difference between average of all even numbers except divisible by 4 and
# average of all odd numbers except divisible by 5 in a list of user defined 20 values?

l=[]
for i in range(20):
    n=int(input("Enter "+str(i+1)+" number to list : "))
    l.append(n)

se=ce=so=co=0
for i in l:
    if (i%2==0 and i%4!=0):
        se=se+i
        ce=ce+1
    if (i%2!=0 and i%5!=0):
        so=so+i
        co=co+1

avgEven=se/ce
avgOdd=so/co
diff=avgEven-avgOdd
print("Difference between average of all even numbers except divisible by 4 and average of all odd numbers except divisible by 5 in a list is",diff)