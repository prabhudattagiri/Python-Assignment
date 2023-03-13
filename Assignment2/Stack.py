MaxSize = 20
stack = []
top = -1

def push(item):
    global top # global keyword is used to access global variable top insted of creating local top variable
    if isfull():
        print("Stack is full.")
        return
    top += 1
    stack.append(item)

def pop():
    global top
    if isempty():
        print("Stack is empty.")
        return
    top -= 1
    return stack.pop()

def isempty():
    return top == -1

def isfull():
    return top == MaxSize - 1

def peak():
    if isempty():
        print("Stack is empty.")
        return
    return stack[top]