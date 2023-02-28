# Sum of product of consecutive digits of any digit number ? Such as n=1234 result =1*2+2*3+3*4
num=int(input("Enter a Number : "))
snum=str(num)
l=len(snum)
sum=0

for i in range(0,l-1):
    t=int(snum[i])*int(snum[i+1])
    sum=sum+t
    i=i+1

print("Sum of product of consecutive digits of ",num," is ",sum)