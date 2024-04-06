"""
Given two Singly Linked List of N and M nodes respectively. The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have same data and with same arrangement too.


Input:
LinkedList1: 1->2->3->4->5->
LinkedList2: 32->59->42->32
Output: Not identical 

"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        

def areIdentical(head1, head2):
    while head1 is not None and head2 is not None:
        if head1.data != head2.data:
            return "Not identical"
        head1 = head1.next
        head2 = head2.next


    if head1 is not None or head2 is not None:
        return "Not identical"

    return "Identical"




def printList(head: Node) -> Node:
    "print a linked list elements"
    temp = head
    while(temp!=None):
        print(temp.data, end =" ")
        temp = temp.next
    print()
    
head = Node(100)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(400)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

head_1 = Node(10)
n1 = Node(20)
n2 = Node(30)
n3 = Node(40)
n4 = Node(90)

head_1.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

print("Original linked list")
printList(head)
printList(head_1)
isIdentical = areIdentical(head, head_1)
print(isIdentical)