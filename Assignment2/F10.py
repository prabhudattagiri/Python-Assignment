# 10.Wap to perform all arithmetic operations using anonymous or lambda function?
sum = lambda a,b :a+b
sub = lambda a,b :a-b
mul = lambda a,b :a*b
div = lambda a,b :a/b
mod = lambda a,b:a%b

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

print("%i + %i = %i" %(a,b,sum(a,b)))
print("%i - %i = %i" %(a,b,sub(a,b)))
print("%i * %i = %i" %(a,b,mul(a,b)))
print("%i / %i = %i" %(a,b,div(a,b)))
print("%i mod %i = %i" %(a,b,mod(a,b)))