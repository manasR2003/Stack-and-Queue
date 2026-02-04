#linkedlist is a linear data structure which stores data as well as address of the next node.
#traversing of elements from linkedlist

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
def travele(head):
    c_node=head
    while c_node:
        print(c_node.value,end='->')
        c_node=c_node.next
    print('NULL')

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6

travele(node1)


#finding minimu value
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def fidele(head):
    min_node = head.value
    c_node = head.next

    while c_node:
        if c_node.value < min_node:
            min_node = c_node.value
        c_node = c_node.next

    return min_node

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", fidele(node1))


#delete specific node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def travele(head):
    c_node=head
    while c_node:
        print(c_node.value,end='->')
        c_node=c_node.next
    print('NULL')

def delenode(head,d_node):
    if head==d_node:
        return head
    c_node=head
    while c_node.next and c_node.next !=d_node:
        c_node=c_node.next
    
    if c_node.next is None:
        return head
    c_node.next=c_node.next.next
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print("Before deletion:")
travele(node1)

# # Delete node4
node1 = delenode(node1, node4)

print("\nAfter deletion:")
travele(node1)