#  To add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string 5. is less than 3, leave it unchanged. 
# Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'

s=input("Enter a string : ")
b=len(s)
if (b>=3):
    if s.endswith("ing"):
        s=s+"ly"
    else:
        s=s+"ing"

print("Modified String is "+s)