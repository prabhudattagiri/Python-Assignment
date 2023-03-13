def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def sqrt(n): #library function
    if n < 0:
        print("Cannot compute square root of a negative number.")
        return
    elif n == 0:
        return 0
    else:
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x

def swap(a, b): # without using 3rd variable
    a = a + b
    b = a - b
    a = a - b
    return a, b
