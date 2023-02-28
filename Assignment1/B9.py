# Write a python program to find repeated numbers as well as frequency of repetition of numbers in a list of 20 user defined values?
l=[]
for i in range(10):
    n=int(input("Enter "+str(i+1)+" number : "))
    l.append(n)

u=list(set(l))
f=[]
for i in u:
    a=l.count(i)
    f.append(a)

rn=[]
fr=[]
for i in range(len(f)):
    if f[i]>1:
        a=f.index(f[i],i) # f[i]=actual value , i=starting position
        n=u[a]
        rn.append(n)
        fr.append(f[i])

print("Given list is ",l)
print("Unique item are",u)
print("Repeated number are",rn)
print("Frequency of repeted Number",fr)