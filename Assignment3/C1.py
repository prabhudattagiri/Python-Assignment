# 1. Wap to findout area and perimeter of a triangle having three sides using class?
import math

class Triangle:
    def __init__(self,a,b,c):
        self.s1=a
        self.s2=b
        self.s3=c

    def perimeter(self):
        self.p=self.s1+self.s2+self.s3
        print("Perimeter of Triangle is ",self.p)

    def area(self):
        s=self.p/2 # semi perimeter s=(s1+s2+s3)/2
        a=math.sqrt(s*(s-self.s1)*(s-self.s2)*(s-self.s3))
        print("Area of of Triangle is ",a)

# In main
x=int(input("Enter the length of Side1 : "))
y=int(input("Enter the length of Side2 : "))
z=int(input("Enter the length of Side3 : "))
t=Triangle(x,y,z)
t.perimeter()
t.area()