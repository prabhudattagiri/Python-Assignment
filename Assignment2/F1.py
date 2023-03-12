# 1. Wap to create a list of prime Fibonacci series between user defined range and default range is 10 to 50 
# using default arguments,required argument,kegyword araguments and function ?
def prime(n):
    if n<=1: # Prime Number always greather than 1
        return False
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return False
    return True

def series(n1=10,n2=50): # Default argument
    # Find all fibonacci number in given range
    fibonacci = [0,1]
    while fibonacci[-1]<n2:
        f=fibonacci[-1]+fibonacci[-2]
        fibonacci.append(f)

    # Find all Prime fibonacci number
    primefib =[]
    for i in fibonacci:
        if (i>=n1 and i<=n2 and prime(i)):
            primefib.append(i)

    return primefib # return prime fibonacci series

#  Calling Function
print("Default argument (10,50)")
a=series()
print(a)
print("Required argument (2,20)")
b=series(2 , 20)
print(b)
print("Keyword argument (5,30)")
c=series(n1=5,n2=30)
print(c)