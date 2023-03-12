# 4. Wap to find repeated elements and no of repeated elements in the list of 20 user defined values and also remove
# redundant values and update list with unique values only using required arguments and pass by reference ?

def findRepeted (l):
    repeted ={} # dictionary type for store both value with frequency
    unique = list(set(l))
    for i in unique:
        count = l.count(i)
        if count >1:
            repeted[i]=count

    for i in repeted: # printing repeted number with frequency
        print(i," is repeted ",repeted[i]," times")
    
    l.clear()
    l.extend(unique) # extend used to assign sequence to list
    print("After remove redundant value the list is ",l)

# Calling function
l=[]
for i in range(1,21):
    a=int(input("Enter "+str(i)+" element to list : "))
    l.append(a)

findRepeted(l)