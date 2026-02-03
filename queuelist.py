#Queue using python list
queue=[]

queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')
queue.append('E')
queue.append('F')

print(queue)

peek=queue[0]
print(peek)

print(queue.pop(0))

print('isempty :',len(queue)==0)


#queue using python class
class Queue:
    def __init__(self):
        self.queue=[]
    
    def push(self,value):
        self.queue.append(value)

    def isempty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
    def pop(self):
        return self.queue.pop(0)
    
myqueue=Queue()
myqueue.push('A')
myqueue.push('B')
myqueue.push('C')
myqueue.push('D')
myqueue.push('E')
print(myqueue.queue)
print(myqueue.isempty())
print(myqueue.pop())
print(myqueue.queue)
print(myqueue.size())


#queue using linkedlist
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.len=0
    
    def isEmpty(self):
        return self.len == 0

    def size(self):
        return self.len

    def enqueue(self,val):
        new_node=Node(val)
        if self.rear is None:
            self.front=self.rear=new_node
            self.len+=1
            return
        self.rear.next=new_node
        self.rear=new_node
        self.len+=1
    def dequeue(self):
        if self.isEmpty():
            return 'queue is empty'
        temp=self.front
        self.front=temp.next
        self.len-=1
        if self.front is None:
            self.rear = None
        return temp.value
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")

print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")

print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())