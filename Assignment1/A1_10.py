# Sum of product of consecutive prime digits of any digit number
num=int(input("Enter a Number : "))
s=str(num)
l=len(s)
sum=0
for i in range(0,l-1):
    d1=int(s[i])
    d2=int(s[i+1])
    prime1=False
    # check d1 is prime or not
    if d1!=1:
        prime1=True
    for i in range(2,d1):
        if d1%i==0:
            prime1 = False
    # check d2 is prime or not
    prime2=False
    if d2!=1:
        prime2=True
    for i in range(2,d2):
        if d2%i==0:
            prime2 = False

    if (prime1 and prime2):
        sum=sum+(d1*d2)

print("Sum of product of consecutive prime digits of",num,"is",sum)