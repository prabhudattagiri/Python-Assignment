# WAP to do following using string
# a) Check whether a string is palindrome or not 
s=input("Enter a String : ")
rev=""
for i in s:
    rev=i+rev
if rev == s:
    print(s,"is palindrome string")
else:
    print(s+" is not palindrome string")