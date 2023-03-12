# 3. Wap to chech wheather a number is palindrome number and divisible by 3 and 5 or
# not using defaunt arguments,required argument,kegyword araguments and function?

def pallindrome(n=525):
    num=n
    pld=0
    while(n!=0):
        pld=pld*10+(n%10)
        n=n//10

    if (num==pld and num%3==0 and num%5==0):
        print(num," is pallindrome and divisibe by 3 and 5")
    else:
        print(num," is not pallindrome or not divisibe by 3 and 5")
        
print("Default argument")
pallindrome()
print("Required argument")
pallindrome(37137)
print("Keyword argument")
pallindrome(n=35553)