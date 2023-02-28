# c) categories the password as low medium and high low – only numbers or alphabets and length less than 8
#  medium- number and alphabets and length more than 8 string- number, alphabet and special character should  
#  present and length should be greater than 8

p=input("Enter your password : ")
l=len(p)

if (p.isdigit==True or p==p.isalpha==True or l<8):
    print("Password is low")
elif (p.isalnum==True and l>8):
    print("Password is medium")
else:
    print("Password is High")