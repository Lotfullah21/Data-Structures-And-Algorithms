"""
Problem description: Input:
LinkedList: 3->3->4->5
Output: 3 4 5
Explanation: In the given linked list 
3 ->3 -> 4-> 5, only 3 occurs more 
than 1 time. So we need to remove it once.

The linked list should be sorted, otherwise this method does not work.

"""

class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
            
def displayList(head: Node):
    "displays elements of a linked list"
    temp = head
    while(temp!=None):
        print(temp.data, end=" ")
        temp = temp.next
        
def removeDup(head: Node):
    "given a sorted linked list, remove duplicates from the linked list"
    curr = head   
    #  curr.next!=None makes sure that there is at least one more element.
    while curr!=None and curr.next!=None:
        if curr.data == curr.next.data:
            plusOnePointer = curr.next.next
            curr.next = plusOnePointer
        else:
            curr = curr.next
    
head = Node(10)
n1 = Node(30)
n2 = Node(30)
n3 = Node(30)
n4 = Node(32)
n5 = Node(30)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Original linked list: ",end=" ")
displayList(head)
removeDup(head)
print("\nLinked list after removing duplicates: ",end =" ")
displayList(head)