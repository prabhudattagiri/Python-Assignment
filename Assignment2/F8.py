# 8. Wap to find area,perimeter of rectangle,square,triangle having 3 sides using keyword arguments with function?
def areaPerimeter (**args):
    shape = args['shape'].lower()

    if shape == 'rectangle':
        l=args['l']
        b=args['b']
        area = l*b
        perimeter = 2 *(l + b)
        print("Area of rectangle:", area)
        print("Perimeter of rectangle:", perimeter)
    
    elif shape == 'square':
        s=args['s']
        area = s ** 2
        perimeter = 4 * s
        print("Area of square:", area)
        print("Perimeter of square:", perimeter)

    elif shape == 'triangle':
        s1 = args['s1']
        s2 = args['s2']
        s3 = args['s3']
        s = (s1 + s2 + s3) / 2
        area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
        perimeter = s1 + s2 + s3
        print("Area of triangle:", area)
        print("Perimeter of triangle:", perimeter)
        
    else:
        print("Invalid shape")

# Calling using keyword arguments
areaPerimeter(shape='rectangle',l=8,b=5)
areaPerimeter(shape='square',s=4)
areaPerimeter(shape='triangle',s1=3,s2=4,s3=5)