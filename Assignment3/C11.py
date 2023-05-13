# 11. WAP to find factorial,GCD,LCM ,generate prime numbers in 
# between user defined range, and generate febonacci series in 
# between user defined range using multiple inheritance?

class Factorial:
    def calculate_factorial(self, n):
        if n < 0:
            return None
        elif n == 0:
            return 1
        else:
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            return fact


class GCD:
    def calculate_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


class LCM:
    def calculate_lcm(self, a, b):
        gcd = GCD().calculate_gcd(a, b)
        lcm = (a * b) // gcd
        return lcm


class Prime:
    def get_primes(self, start, end):
        prime_list = []
        for num in range(start, end + 1):
            if self.is_prime(num):
                prime_list.append(num)
        return prime_list

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True


class Fibonacci:
    def fibonacci_series(self, start, end):
        fibonacci_list = []
        a, b = 0, 1
        while a <= end:
            if a >= start:
                fibonacci_list.append(a)
            a, b = b, a + b
        return fibonacci_list


class MathOperations(Factorial, GCD, LCM, Prime, Fibonacci):
    pass


# In main
mathObj = MathOperations()

num = int(input("Enter a number : "))
factorial = mathObj.calculate_factorial(num)
print("Factorial of ",num,"is :", factorial)

# GCD & LCM
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
gcd = mathObj.calculate_gcd(a, b)
print(f"GCD of ",a," and ",b,"is :", gcd)

lcm = mathObj.calculate_lcm(a, b)
print("LCM of ",a," and ",b,"is :", lcm)

# Prime number
start, end = 10, 50 # can take from user
prime_list = mathObj.get_primes(start, end)
print(f"Prime numbers between ",start," and ",end,"are :", prime_list)

# Fibonacci
start, end = 0, 100
fibonacci_series = mathObj.fibonacci_series(start, end)
print("Fibonacci series between ",start," and ",end," are :", fibonacci_series)
