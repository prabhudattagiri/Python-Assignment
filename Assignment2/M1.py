# 1. WAP to create scientific calculator and perform all arithmetic operations like sum,subtraction,division,multiplication,
# modulus,power,sqrt,cubic root,sinx,cos x,tanx,log x,exp x,absolute value of x using function and module?

import Arithmetic as Art
# Display all option
print("Scientific Calculator Menu")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
print("6. Power")
print("7. Square Root")
print("8. Cubic Root")
print("9. Sine")
print("10. Cosine")
print("11. Tangent")
print("12. Logarithm")
print("13. Exponential")
print("14. Absolute Value")
print("0. Exit")

choice = int(input("Enter choice (1-14): "))
num1 = float(input("Enter first number: "))

if choice in [7, 8, 9, 10, 11, 13, 14]:
    # If operation requires only one operand
    result = None
    if choice == 7:
        result = Art.sqrt(num1)
    elif choice == 8:
        result = Art.cbrt(num1)
    elif choice == 9:
        result = Art.sin(num1)
    elif choice == 10:
        result = Art.cos(num1)
    elif choice == 11:
        result = Art.tan(num1)
    elif choice == 13:
        result = Art.exp(num1)
    elif choice == 14:
        result = Art.absolute(num1)
    
    # Print result
    print("Result: ", result)

else:
    # If operation requires two operands
    num2 = float(input("Enter second number: "))

    result = None
    if choice == 1:
        result = Art.add(num1, num2)
    elif choice == 2:
        result = Art.subtract(num1, num2)
    elif choice == 3:
        result = Art.multiply(num1, num2)
    elif choice == 4:
        result = Art.divide(num1, num2)
    elif choice == 5:
        result = Art.modulus(num1, num2)
    elif choice == 6:
        result = Art.power(num1, num2)
    
    # Print result
    print("Result: ", result)