"""
Given two linked lists of size n1 and n2 respectively, you have to join the head of second list to the tail of first so that we can traverse both the lists using head of 1st list.

Example 1:

Input:
LinkedList1: 1->3->8
LinkedList2: 3->4
Output: 1 3 8 3 4

"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
def joinTheLists(head1, head2):
    temp = head1
    while (temp.next!=None):
        temp = temp.next
    temp.next = head2
    return head1



def maximum(head):
    "returns maximum element in a linked list."
    temp = head
    current_max = float('-inf')
    while (temp!=None):
        if temp.data>current_max:
            current_max = temp.data
        temp = temp.next
    return current_max
    
    
def minimum(head):
    "returns minimum element in a linked list."
    temp = head
    current_min = float('inf')
    while (temp!=None):
        if temp.data<current_min:
            current_min = temp.data
        temp = temp.next
    return current_min

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

head_1 = Node(100)
n1 = Node(90)
n2 = Node(80)
n3 = Node(70)

head_1.next = n1
n1.next = n2
n2.next = n3

print("Original linked list")
printList(head)

print("Two joined linked lists")
joinedList = joinTheLists(head, head_1)
printList(joinedList)
print(maximum(head))
print(minimum(head))