# Difference between Sum of product of consecutive even digits except 2 and 6 and Sum of product
# of consecutive odd digits except 3 and 7 of any digit number
num=int(input("Enter a Number : "))
s=str(num)
l=len(s)
esum,osum=0,0
for i in range(0,l-1):
    d1=int(s[i])
    d2=int(s[i+1])
    if (d1%2==0 and d2%2==0) and ((d1!=2 and d1!=6) and (d2!=2 and d2!=6)):
        esum=esum+(d1*d2)
    if (d1%2!=0 and d2%2!=0) and ((d1!=3 and d1!=7) and (d2!=3 and d2!=7)):
        osum=osum+(d1*d2)
diff=esum-osum
print("Sum of product of consecutive even digits except 2 and 6 and Sum of product of of consecutive odd digits except 3 and 7",num,"is",diff)