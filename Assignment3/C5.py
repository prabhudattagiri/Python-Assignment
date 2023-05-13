# 5. WAP to compute number of objects of a class has been created 
# using data hiding technique of class?

class MyClass:
    # private class variable
    __count =0
    def __init__(self):
        MyClass.__count+=1 # increase on create object
    
    # static method (call by class name)
    def totalObject():
        return MyClass.__count

# in main
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print("Total no of object created = ",MyClass.totalObject())