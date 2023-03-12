# 6. Wap to find factorial of a number using while loop,do while loop and for loop and keyword arguments function?
def whileloop(n):
    f=1
    while n>1:
        f=f*n
        n=n-1
    
    return f

# There is no do while loop in python

def forloop(n):
    f=1
    for i in range(2,n+1):
        f=f*i
        
    return f

# Calling function
print("Factorial of 5 using while loop is ",whileloop(n=5)) # keyword argument
print("Factorial of 7 using for loop is ",forloop(n=7))