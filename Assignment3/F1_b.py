# b) Read the content of number.txt file as a string file and split them into 3 
# numbers. Then find factorial of difference between largest and smallest among 3 
# numbers. Finally append the factorial as factorial=obtained factorial in number.txt

import math
# read the text file
with open("number.txt",'r') as f:
    data = f.read()
# split the data into three number (list)
numbers = data.split(",") 
# convert into int (default is string)
numbers = [int(num) for num in numbers]
# find factorial of difference between largest and smallest
l = max(numbers)
s = min(numbers)
diff = l-s
fact =1
for i in range(2,diff+1):
    fact=fact*i

# Append the factorial to the file
with open('number.txt','a') as f:
    f.write("\nFactorial = "+str(fact))

print("Find Factorial of difference between largest & smallest and Append it to text file successfully")