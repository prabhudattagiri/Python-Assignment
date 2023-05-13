# 2. Wap to findout area and perimeter of a rectangle and square using class ?

class Rectangle:
    def __init__(self,a,b):
        self.l=a
        self.b=b

    def perimeter(self):
        p=2*(self.l+self.b)
        print("Perimeter of Rectangle is ",p)

    def area(self):
        a=self.l*self.b
        print("Area of Rectangle is ",a)

class Square:
    def __init__(self,a):
        self.s=a

    def perimeter(self):
        p=4*self.s
        print("Perimeter of Square is ",p)

    def area(self):
        a=self.s*self.s
        print("Area of Square is ",a)

# In main
x=int(input("Enter the length of Rectangle : "))
y=int(input("Enter the breadth of Rectangle : "))
r=Rectangle(x,y)
r.perimeter()
r.area()
z=int(input("Enter the side of Square : "))
s=Square(z)
s.perimeter()
s.area()