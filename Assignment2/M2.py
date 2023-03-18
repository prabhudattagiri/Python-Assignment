# 2. WAP to perform following computation on stack using function like
# push, pop, isempty, isfull, peak and use function and module
# I. Create an stack of user defined size using list
# II. Insert 20 user defined values in the stack using is full and push operation in stack
# III. Search for an user defined element in the stack using peak operation of stack
# IV. Delete 5 elements from stack using pop opeartion
# V. Display all remaig elements of stack

import Stack as st

# create stack of user defined size
size = int(input("Enter the size of the stack : "))
st.MaxSize = size

# insert 20 user defined values in the stack using is full and push operation
for i in range(size):
    n=int(input("Enter "+str(i+1)+" element to Stack :"))
    if st.isfull():
        print("Stack is Full")
        break
    st.push(n)

# search for an user defined element in the stack using peak operation of stack
value =int(input("Enter the value to search in the stack : "))
found = False
for i in range(st.top,-1,-1):
    if st.stack[i] == value:
        print(value," is found at index ",i)
        found = True
        break

if not found:
    print(value," not found in the stack")

# delete 5 elements from stack using pop operation
for i in range(5):
    if st.isempty():
        print("Stack is empty")
        break
    st.pop()

# display all remaining elements of stack
print("Remaining elements of the stack :")
for i in range(st.top,-1,-1):
    print(st.stack[i])