"""
Problem description: Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->9->11
Output: 8
Explanation: In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 9.  
If n>len, return -1
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def displayList(head):
    curr = head
    while curr!=None:
        print(curr.data, end=" ")
        curr = curr.next
    
    
def findNthNode(head:Node, n: int) -> Node:
    "find the Nth node from last point of a linked list."
    curr = head
    len = 0
    while curr!=None:
        len = len + 1
        curr = curr.next
    if n>len:
        return -1
    curr = head
    for _ in range(1, len-n+1):
        curr = curr.next
    print(curr.data)
        
    
# Using two pointers 
def findNthNodeTwoPointers(head: Node, n: int) -> Node:
    "find nth node from last position using two pointers"
    if head is None:
        return
    first = head 
    # First, move the first pointer n-step ahead.
    for _ in range(n):
        # handle if n>len
        if first==None:
            return 
        first = first.next
    second = head
    # until first did not reach to the end, continue and move each of the pointers just one step at a time.
    while (first!=None):
        first = first.next
        second = second.next
    print(second.data)
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)
temp4 = Node(50)
head.next = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
print("Original linked list: ",end=" ")
displayList(head)
print("\nNth node:")
findNthNode(head,52)
findNthNodeTwoPointers(head,1)