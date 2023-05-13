# 3. Wap to display the order in which constructors and destructors are invoked during runtime in class ?

class MyClass:
    def __init__(self, name):
        self.name = name
        print("Constructor invoked for", self.name)
    
    def __del__(self):
        print("Destructor invoked for", self.name)

# Example usage
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")