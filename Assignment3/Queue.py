# 2. WAP to perform following computation on queue using function like insert, 
# delete, isempty, isfull, peak and use class and object with multiple inheitence
# VI. Create an queue of user defined size using list
# VII. Insert 20 user defined values in the queue using is full and insert 
# operation in queue
# VIII. Search for an user defined element in the queue using peak 
# operation of queue
# IX. Delete 5 elements from queue using delete opeartion
# X. Display all remain elements of queue

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def insert(self, item):
        if not self.is_full():
            self.queue.append(item)
            print("Inserted item: " + str(item))
        else:
            print("Queue is full. Cannot insert item.")

    def delete(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print("Deleted item: " + str(item))
        else:
            print("Queue is empty. Cannot delete item.")

    def peak(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None


class UserQueue(Queue):
    def __init__(self, size):
        super().__init__(size)

    def insert_values(self, values):
        for value in values:
            if not self.is_full():
                self.insert(value)
            else:
                print("Queue is full. Cannot insert more values.")
                break


# Create a user-defined queue of size 20
queue_size = 20
user_queue = UserQueue(queue_size)

# Insert 20 user-defined values in the queue
values = []
for i in range(queue_size):
    value = input("Enter value to "+(i+1)+" element : ")
    values.append(value)
user_queue.insert_values(values)

# Search for a user-defined element in the queue
search_value = input("Enter a value to search in the queue: ")
if search_value in user_queue.queue:
    print(search_value + " is found in the queue.")
else:
    print(search_value + " is not found in the queue.")

# Delete 5 elements from the queue
for i in range(5):
    user_queue.delete()

# Display all remaining elements of the queue
print("Remaining elements in the queue:")
while not user_queue.is_empty():
    print(user_queue.delete())
