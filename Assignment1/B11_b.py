# b) capitalize first and last character of each word in string
s=input("Enter a string : ")
subs=s.split(" ")
caps=[]
for i in subs:
    if len(i)>2:
        t=i[0].upper()+i[1:-1]+i[-1].upper()
        caps.append(t)
    else:
        if len(i)==1: # for single character
            t=i[0].upper()
            caps.append(t)
        else: # for double character
            t=i[0].upper()+i[-1].upper()
            caps.append(t)

caps=" ".join(caps)    
        
print("After capitalize first and last character of each word in string is ",caps)