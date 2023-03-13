MaxSize = 20
queue = []
front = rear = -1

def insert(item):
    global rear
    if isfull():
        print("Queue is full.")
        return
    if isempty():
        front = rear = 0
    else:
        rear += 1
    queue.insert(rear, item)

def delete():
    global front, rear
    if isempty():
        print("Queue is empty.")
        return
    item = queue.pop(front)
    if front > rear:
        front = rear = -1
    else:
        rear -= 1
    return item

def isempty():
    return front == -1 and rear == -1

def isfull():
    return rear == MaxSize - 1

def peak():
    if isempty():
        print("Queue is empty.")
        return
    return queue[front]