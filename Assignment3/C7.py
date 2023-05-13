# 7. Wap to findout volume of a box using simple inheritance ?
class Shape:
    def __init__(self,a,b,c):
        self.ln=a
        self.br=b
        self.ht=c

    def volume(self):
        vol = self.ln * self.br * self.ht
        return vol
    
class Box(Shape):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

# in main
l = int(input("Enter the length of the box: "))
b = int(input("Enter the breadth of the box: "))
h = int(input("Enter the height of the box: "))

bx = Box(l,b,h)
print("Volume of the Box is ",bx.volume())