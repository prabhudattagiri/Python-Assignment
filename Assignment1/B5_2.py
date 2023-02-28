# To get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
s=input("Enter a string : ")
s1=s[0]
s2=s[1:]
s2=s2.replace(s1,'$')
s=s1+s2
print("After change all occurrences the string is "+s)