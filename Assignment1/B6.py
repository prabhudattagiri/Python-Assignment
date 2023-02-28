#  Write a python program to store names of 10 fruits in strings and sort in alphabetical order
l=[]
for i in range(10):
    f=input("Enter "+str(i+1)+" Fruit Name : ")
    l.append(f)

l.sort()
sortedFruit=" ".join(l)
print(sortedFruit)