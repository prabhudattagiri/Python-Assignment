# 1. WAP to perform following computation on stack using function like push, 
# pop, isempty, isfull, peak and use class and objects and multilevel inheritence
# I. Create an stack of user defined size using list
# II. Insert 20 user defined values in the stack using is full and push 
# operation in stack
# III. Search for an user defined element in the stack using peak 
# operation of stack
# IV. Delete 5 elements from stack using pop opeartion
# V. Display all remain elements of stack

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
            print("Pushed item: " + str(item))
        else:
            print("Stack is full. Cannot push item.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print("Popped item: " + str(item))
        else:
            print("Stack is empty. Cannot pop item.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None


class UserStack(Stack):
    def __init__(self, size):
        super().__init__(size)

    def insert_values(self, values):
        for value in values:
            if not self.is_full():
                self.push(value)
            else:
                print("Stack is full. Cannot insert more values.")
                break


# Create a user-defined stack of size 20
stack_size = 20
user_stack = UserStack(stack_size)

# Insert 20 user-defined values in the stack
values = []
for i in range(stack_size):
    value = input("Enter value to "+(i+1)+" element : ")
    values.append(value)
user_stack.insert_values(values)

# Search for a user-defined element in the stack
search_value = input("Enter a value to search in the stack: ")
if search_value in user_stack.stack:
    print(search_value + " is found in the stack.")
else:
    print(search_value + " is not found in the stack.")

# Delete 5 elements from the stack
for i in range(5):
    user_stack.pop()

# Display all remaining elements of the stack
print("Remaining elements in the stack:")
while not user_stack.is_empty():
    print(user_stack.pop())
