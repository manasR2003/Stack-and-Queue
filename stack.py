#stack using python list

stack=[]

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
stack.append('F')

print(stack)

print('peek :',stack[-1])

print('isempty :',len(stack)==0)

print('size :',len(stack))

print(stack.pop())

print(stack)

print('peek :',stack[-1])

print(stack.pop())

print('isempty :',len(stack)==0)

print('size :',len(stack))

##using python class
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,val):
        self.stack.append(val)

    def isempty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def pop(self):
        if self.isempty():
            return 'stack is empty'
        return self.stack.pop()
    
mystack=Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
mystack.push('D')
mystack.push('E')
print(mystack.stack)
print(mystack.isempty())
print(mystack.size())
print(mystack.pop())
print(mystack.stack)
print(mystack.size())

#Stack using linkedlist

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def pop(self):
        if self.isempty():
            return 'Stack is empty'
        popped_node=self.head
        self.head=self.head.next
        self.size-=1
        return popped_node.value
    
    def isempty(self):
        return self.size==0
    
    def stacksize(self):
        return self.size
    
mystack=Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
mystack.push('D')
mystack.push('E')

print(mystack.stacksize())
print(mystack.isempty())

print(mystack.pop())
