# Write a python program to create a tuple of constants values like pi and exponent and use them to find area and perimeter of circle?
import math
v=(3.141,2.718) # value of pi & e
r=int(input("Enter the radius of the circle : "))
a=v[0]*r*r
p=2*v[0]*r
a=round(a,2)
p=round(p,2)
print("Area of circle is ",a)
print("Perimeter of circle is ",p)