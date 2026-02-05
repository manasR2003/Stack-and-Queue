# #tree is non linear data structure .
# #example : File system,HTML DOM

# #Basic tree terminology
# # node=element in tree
# # root=topmost element
# # parent=element with child node
# # child=element with parent node
# # subtree=part of a tree
# # leaf=node  that hasnot any child node
# # height=path from root to leaf
# # weidth=distance from root to node

# #types of tree  1.binary tree  2.binary search tree 
# #binary tree
# #-each node having t most 2 child node left and right

# #creating binary tree
# class Node:
#     def __init__(self,value):
#         self.left=None
#         self.right=None
#         self.value=value

# node1=Node(9)
# node2=Node(11)
# node3=Node(1)
# node4=Node(0)
# node5=Node(-1)
# node6=Node(19)
# node7=Node(91)

# node1.left=node2
# node1.right=node3

# node2.left=node4
# node2.right=node5

# node3.left=node6
# node3.right=node7

# #traversing binary tree
# #inorder
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.value,end=' ')
#         inorder(root.right)
# inorder(node1)
# print('-----------------------------------')
# #preorder
# def preorder(root):
#     if root:
#         print(root.value,end=' ')
#         preorder(root.left)
#         preorder(root.right)
# preorder(node1)
# print('-----------------------------------')

# #postorder
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.value,end=' ')
# postorder(node1)

# #binary search tree
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.value:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root
root = None   # start with empty tree

values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = insert(root, v)

#inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

inorder(root)
print()
#preorder
def preorder(root):
    if root:
        print(root.value,end=' ')
        preorder(root.left)
        preorder(root.right)
preorder(root)
print()

#postorder
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end=' ')
postorder(root)