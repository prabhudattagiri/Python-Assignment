#  Write a python program to create a list of prime numbers as per given range
s=int(input("Enter starting index : "))
e=int(input("Enter ending index : "))
l=[]
for i in range(s,e):
    prime=False
    if i>1:
        prime=True
    for j in range(2,i):
        if(i%j==0):
            prime=False
    if(prime):
        l.append(i)

print("Item in the list is",l)