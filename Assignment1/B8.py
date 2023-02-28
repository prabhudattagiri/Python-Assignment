#  Write a python program to find 1st,2nd and 3rd largest and smallest numbers in a list 20 user defined values.
l=[]
for i in range(20):
    a=int(input("Enter "+str(i+1)+" Number : "))
    l.append(a)

l.sort()
print("1st largest is %d 2nd largest is %d 3rd largest is %d"%(l[19],l[18],l[17]))
print("1st smallest is %d 2nd smallest is %d 3rd smallest is %d"%(l[0],l[1],l[2]))