
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def displayList(head):
    curr = head
    result = []
    while curr!=None:
        result.append(curr.data)
        curr = curr.next
    return result
    
    
def findNthNode(head:Node, n: int) -> Node:
    "find the Nth node from last point of a linked list."
    NodeCount = 0
    curr = head
    while curr!=None:
        NodeCount = NodeCount + 1
        curr = curr.next
    print("number of nodes =",NodeCount)
    curr = head
    if n>NodeCount:
        return
    for _ in range(1, NodeCount-n+1):
        curr = curr.next
    return curr.data
        
    
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
    return second.data
    
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("Original linked list")
linkedList = displayList(head)
for ele in linkedList:
    print(ele, end=">")
print()

n = 2
nthNode =findNthNode(head,n)
print(f"{n}nd node from left side is {nthNode}")
