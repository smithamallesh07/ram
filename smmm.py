'''def binary_search(arr, low, high, x):
    if(low<=high):
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, low, x)
    else:
        return -1
arr=[]
n=int(input("enter the element:"))
for i in range(n):
    value=int(input("enter the elment:"))
    arr.append(value)
arr.sort()
print("sorted array:", arr)
x=int(input("enter value to search:"))
result=binary_search(arr, 0, len(arr)-1, x)
if(result!=-1):
    print("element is present:")
else:
    print("element is not present:")'''


stack=[]
n=int(input("enter the code:"))
while n!=4:
    if(n==1):
        value=int(input("enter the element to push:"))
        stack.append(value)
        n=int(input("enter the code:"))
    elif(n==2):
        if len(stack)!=0:
            print("deleted element:")
            print(stack.pop(0))
            n=int(input("enter the code:"))
        else:
            print("empty stack")
        n=int(input("enter the code:"))
    elif(n==3):
        if len(stack)!=0:
            print("content of stack")
            print(stack)
            n=int(input("enter the code:"))
        else:
            print("empty stack")
            n=int(input("enter the code:"))
    else:
        break


'''queue=[]
n=int(input("code"))
while n!=4:
    if n==1:
        value=int(input("enter the element to push:"))
        queue.append(value)
        n=int(input("code"))
    elif n==2:
        if len(queue)!=0:
            print("deleted element:")
            print(queue.pop(0))
            n=int(input("code"))
        else:
            print("empty queue")
            n=int(input("code"))
    elif n==3:
        if len(queue)!=0:
            print("content of queue:")
            print(queue)
            n=int(input("code"))
        else:
            print("empty queue")
            n=int(input("code"))
    else:
        break'''
