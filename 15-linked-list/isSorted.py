"""

Given a linked list of size n, you have to find whether the given linked list is sorted or not.
The sorting can either be non-increasing or non-decreasing.

Example 1:

Input:
LinkedList: 5->5->6->7->8
Output: 1

"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
def isSorted(head):
    curr = head
    increasing = None  

    while curr.next is not None:
        if curr.data == curr.next.data:
            curr = curr.next
            continue

        if curr.data < curr.next.data:
            if increasing is None:
                increasing = True
            elif not increasing:
                return 0  
        else:
            if increasing is None:
                increasing = False
            elif increasing:
                return 0  
        curr = curr.next
    return 1 
        
        
def printList(head: Node) -> Node:
    "print a linked list elements"
    temp = head
    while(temp!=None):
        print(temp.data, end =" ")
        temp = temp.next
    print()
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("Original linked list")
printList(head)


print("Is sorted?: ",isSorted(head))

