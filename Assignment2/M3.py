# 3. WAP to perform following computation on queue using function like insert, 
# delete, isempty, isfull, peak and use function and module
# VI. Create an queue of user defined size using list
# VII. Insert 20 user defined values in the queue using is full and insert operation in queue
# VIII. Search for an user defined element in the queue using peak operation of queue
# IX. Delete 5 elements from queue using delete opeartion
# X. Display all remaig elements of queue

import Queue as qu
# create queue of user defined size
size = int(input("Enter the size of the queue: "))
qu.MaxSize = size

# insert 20 user defined values in the queue using is full and insert operation
for i in range(size):
    value = int(input("Enter "+str(i+1)+" element to Queue : "))
    if qu.isfull():
        print("Queue is full.")
        break
    qu.insert(value)

# search for an user defined element in the queue using peak operation of queue
value = int(input("Enter the value to search in the queue: "))
found = False
for i in range(qu.front, qu.rear+1):
    if qu.queue[i] == value:
        print(value,"found at index ",i)
        found = True
        break
if not found:
    print(value," not found in the queue.")

# delete 5 elements from queue using delete operation
for i in range(5):
    if qu.isempty():
        print("Queue is empty.")
        break
    qu.delete()

# display all remaining elements of queue
print("Remaining elements of the queue:")
for i in range(qu.front, qu.rear+1):
    print(qu.queue[i])