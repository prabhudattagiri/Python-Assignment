# 4. Wap to swap two numbers without using 3rd variable and with using 3rd variable using class?

class Swap:
    def __init__(self,x,y):
        self.a=x
        self.b=y

    def swapwith(self):
        print("Before swapping with 3rd variable value of a is ",self.a,"and b is ",self.b)
        temp=self.a
        self.a=self.b
        self.b=temp
        print("After swapping with 3rd variable value of a is ",self.a,"and b is ",self.b)
    def swapwithout(self):
        print("Before swapping without 3rd variable value of a is ",self.a,"and b is ",self.b)
        self.a=self.a+self.b
        self.b=self.a-self.b
        self.a=self.a-self.b
        print("After swapping without 3rd variable value of a is ",self.a,"and b is ",self.b)

# In main
x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
# Crate 2 object for calling 2 method
s1=Swap(x,y)
s1.swapwith()
s2=Swap(x,y)
s2.swapwithout()