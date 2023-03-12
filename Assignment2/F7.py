# 7. Wap to search position of element in the list of 20 user defined values using binary serach and function?
def binary (arr,low,high,x):
    if high >=low:
        mid = (high+low)//2
        
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary(arr,low,mid-1,x)
        else:
            return binary(arr,mid+1,high,x)
    else:
        return -1
    
# Calling Function
arr =[]
for i in range(20):
    a=int(input("Enter "+str(i+1)+" element : "))
    arr.append(a)

n=int(input("Enter a number to search in the list : "))
result = binary(arr,low=0,high=19,x=n)

if result == -1:
    print("Element is not present in the list")
else:
    print("Element is present at index ",result)