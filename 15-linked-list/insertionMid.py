"""
Given a linked list of size N and a key. The task is to insert the key in the middle of the linked list.

Example 1:

Input:
LinkedList = 1->2->4
key = 3
Output: 1 2 3 4
Explanation: The new element is inserted
after the current middle element in the
linked list.

"""

class Node:
    def __init__(self, val):
        self.key = val
        self.next = None
        
def insertInMid(head,node):
    newNode = Node(node)
    # handling the case if list is empty.
    if head==None:
        head = node
        return head
    # pointers.
    slow = head
    fast = head 
    # fast.next.next to keep the pointer one step behind the mid, because we want to replace mid.
    while fast!=None and fast.next!=None and fast.next.next!=None:
        slow = slow.next
        fast = fast.next.next
    next = slow.next
    slow.next = newNode
    newNode.next = next
    return head



def printList(head: Node) -> Node:
    "print a linked list elements"
    temp = head
    while(temp!=None):
        print(temp.key, end =" ")
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


newList = insertInMid(head,90)
print("Reversed linked list")
printList(newList)