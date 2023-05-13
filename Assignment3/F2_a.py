# 2. WAP to do following using file handling
#  a) create a file Myself.txt and store information about your received through 
#     terminal

f = open("Myself.txt",'w')
name = input("Enter Your Name : ")
age = input("Enter Your Age : ")
city = input("Enter Your City : ")
details = name+"\n"+age+"\n"+city
f.write(details)
f.close