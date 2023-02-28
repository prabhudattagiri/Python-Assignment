# Sum of product of consecutive odd digits of any digit number
num=int(input("Enter a Number : "))
s=str(num)
l=len(s)
sum=0
for i in range(0,l-1):
    d1=int(s[i])
    d2=int(s[i+1])
    if (d1%2!=0 and d2%2!=0):
        sum=sum+(d1*d2)

print("Sum of product of consecutive odd digits of",num,"is",sum)