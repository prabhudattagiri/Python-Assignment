import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def modulo(x, y):
    return x % y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Invalid input"
    else:
        return math.sqrt(x)

def cubic_root(x):
    return x ** (1/3)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def log(x):
    if x <= 0:
        return "Invalid input"
    else:
        return math.log(x)

def exp(x):
    return math.exp(x)

def absolute(x):
    return abs(x)