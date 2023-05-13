# 9. Wap to findout area and perimeter of rectangle and square using method overriding and abstract class ?
from abc import ABC
class Shape(ABC): # Abstract Class
    # abstract method
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,a,b):
        self.ln=a
        self.br=b
    def area(self):
        a=self.ln * self.br
        print("Area of Rectangle is ",a)
    def perimeter(self):
        p=2*(self.ln + self.br)
        print("Perimeter of Rectangle is ",p)

class Square(Shape):
    def __init__(self,a):
        self.s=a
    def area(self):
        a=self.s * self.s
        print("Area of Square is ",a)
    def perimeter(self):
        p=4 * self.s
        print("Perimeter of Square is ",p)

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