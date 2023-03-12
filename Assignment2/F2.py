# 2. Wap to chech wheather a number is Armstrong number or not using default 
# arguments,required argument,kegyword arguments and function?
def armstrong(n=245):
    num=n
    arm=0
    while(n!=0):
        t=n%10
        arm=arm+(t**3)
        n=n//10

    if (num==arm):
        print(num," is an armstrong number")
    else:
        print(num," is not an armstrong number")

print("Default argument")
armstrong()
print("Required argument")
armstrong(121)
print("Keyword argument")
armstrong(n=371)