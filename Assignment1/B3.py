# Write a python program to store details of a student like rollno, regdno, 
# name, branch, stream, sem, phone no,address in dictionary and print the details in cv format
n=input("Enter Your Name : ")
rn=input("Enter Your Roll No : ")
rd=input("Enter Your Regd NO : ")
b=input("Enter Your Branch : ")
st=input("Enter Your Stream : ")
sm=input("Enter Your Semester : ")
ph=input("Enter Your Phone Number : ")
ads=input("Enter Your Address(city/state/pin) :")

student ={"Name":n,"RollNo":rn,"RegdNo":rd,"Branch":b,"Stream":st,"Semester":sm,"Phone":ph,"Address":ads}
print("  CV  \nName :",student["Name"],"\nRoll No :",student["RollNo"],"\nRegd No",student["RegdNo"],"\nBranch :",student["Branch"],"\nStream :",student["Stream"],
      "\nSemester :",student["Semester"],"\nPhone :",student["Phone"],"\nAddress :",student["Address"])