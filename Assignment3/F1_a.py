# 1. WAP to do following using file handling
# a) create a file number.txt and store 3 user defined numbers joined using ‘,’.

a = input("Enter first Number : ")
b = input("Enter second Number : ")
c = input("Enter third Number : ")
# Join the number using " , "
number = ' , '.join([a,b,c])
# Write 3 number in a text file
f = open("number.txt",'w')
f.write(number)
f.close
print("Store 3 User defined number in a text file successfully")