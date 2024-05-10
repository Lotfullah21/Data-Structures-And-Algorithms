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
        
def insertSorted(head, x):
    newNode = Node(x)
    if head is None:
        return newNode
    elif newNode.data<head.data:
        newNode.next = head
        return newNode
    else:
        curr = head
        # Important to first check if the curr.next!=None
        while curr.next!=None and curr.next.data<newNode.data:
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode
        return head



def displayList(head: Node) -> Node:
    "Returns a linked list' data"
    temp = head
    result  = []
    while(temp!=None):
        result.append(temp.data)
        temp = temp.next
    return result

head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)


head.next = temp1
temp1.next = temp2
temp2.next = temp3

linkedList = displayList(head)
print("Linked list before element insertion")
for ele in linkedList:
    print(ele, end=">")
print()


newLinkedList = insertSorted(head, -1)
linkedList = displayList(newLinkedList)
print("Linked list before element insertion")
for ele in linkedList:
    print(ele, end=">")
print()