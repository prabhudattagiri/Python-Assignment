# 9. WAP to swap two numbers using anonymous or lambda function?

n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
print("Before swapping, n1 =", n1, "and n2 =", n2)

n1, n2 = (lambda x: (x[1], x[0]))((n1, n2))

print("After swapping, n1 =", n1, "and n2 =", n2)
