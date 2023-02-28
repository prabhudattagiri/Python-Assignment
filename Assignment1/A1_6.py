# Find kth digit from frontside or back side of any digits number and find its poistional value
num=input("Enter a Number :")
k=input("Enter digit to Search :")
ch=input("Enter Your choice (f=frontside b=backside) : ")
i=p=0
if (ch=='f'or"F"):
    i=num.index(k)
    p=i+1
elif (ch=='b'or"B"):
    i=num.rindex(k)
    p=len(num)-i
else:
    print("You enter invalid choice")

ps=(10**p)

print("Index of",k,"in",num,"is",i,"and positional value is ",ps)
