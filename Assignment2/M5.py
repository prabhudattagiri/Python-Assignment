# 5. Wap to compute factorial,GCD,LCM,sqrt without using any library function,swap 
# two number without using 3rd variable using function and module?

import Compute as cm
n=int(input("Enter a number for find factorial : "))
print("Factorial of ",n," is ",cm.factorial(n))
s=int(input("Enter a number for find Square root : "))
print("Square root of ",n," is ",cm.sqrt(s))
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("GCD of ",a," and ",b," is",cm.gcd(a,b))
print("LCM of ",a," and ",b," is",cm.lcm(a,b))
print("Before swapping value of a and b is ",a," ",b)
a,b=cm.swap(a,b)
print("Before swapping value of a and b is ",a," ",b)