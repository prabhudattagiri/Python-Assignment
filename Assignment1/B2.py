# Write a python program to find total and average mark of a student and take 
# 5 different subject along with marks of 10 students using dictionary
r=[101,102,103,104,105,106,107,108,109,110]
# n=['Abhishek','Bibhuti','Debasish','Gaurav','Jiban','Narendra','Prabhu','Prasanta','Rabindra','Shakti']
s1=[78,88,93,87,65,77,90,84,88,90]
s2=[90,93,88,84,93,87,65,77,90,84]
s3=[67,45,76,81,66,79,58,74,55,72]
s4=[65,77,90,76,81,66,79,83,77,65]
s5=[77,90,84,45,76,81,66,88,93,87]
avg=[]
tm=[]
for i in range(10):
    t=s1[i]+s2[i]+s3[i]+s4[i]+s5[i]
    a=t/5
    avg.append(a)
    tm.append(t)

d={"RollNo":r,"Sub1":s1,"Sub2":s2,"Sub3":s3,"Sub4":s4,"Sub5":s5,"TotalMark":tm,"AvgMark":avg}
print(d)