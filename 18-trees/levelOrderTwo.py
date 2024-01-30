

"""
Level Order Traversal: in this method, the elements are printed level vise.
first print all elements in first level, then 2nd level and so on.
what do I mean by this could be explained in the following example

Input:
    1     ----- level 1 
  /   \ 
 3     2  ----- level 2
Output:1 3 2

Example 2:
Input:

        10      ---- level 1
     /     \
    70      60  ---- level 2
  /   \
 80   90        ---- level 3
Output:10 70 60 80 90


Solution: 

step one: initialize a queue data structure with the root Node
at each iteration
step one: remove an element, removal should be based on queue data structure: first in, first out.
step two: add or print that node's data
step three: add the child of removed element if exist back to the queue.

"""
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
        sizeOfQ = len(q)
        for _ in range(sizeOfQ):
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
        print()
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
