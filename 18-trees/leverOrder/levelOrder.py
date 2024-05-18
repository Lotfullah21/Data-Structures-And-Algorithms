from collections import deque

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def levelOrder(root: Node) -> int:
    q = deque()
    # initialize queue with root node
    q.append(root)
    poppedEle = []
    # until there is element in queue
    while (len(q)>0):
        # remove the first element.
        removedEle = q.popleft()
        print(removedEle.data,end=" ")
        poppedEle.append(removedEle.data)
        # if left child of removed element exists, add it to the queue.
        if removedEle.left:
            q.append(removedEle.left)
        # if right child of removed element exists, add it to the queue.
        if removedEle.right:
            q.append(removedEle.right)
    return poppedEle
        
        
        
# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.right.right = Node(7)

x = levelOrder(root)
