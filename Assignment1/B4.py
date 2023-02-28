# Write a Python program to print and store ‘n terms of Fibonacci series in list
n=int(input("Enter the n terms upto print Fibonacci Series : "))
f1,f2=0,1
l=[]
count=0
while count<n:
    f=f1+f2
    l.append(f)
    f1=f2
    f2=f
    count=count+1

print(l)