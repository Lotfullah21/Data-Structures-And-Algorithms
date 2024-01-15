class Node:
    def __init__(self, val):
        self.key = val
        self.next = None
        
    
def reverseLinkedList(head: Node) -> Node:
    "reverse and return a new linked list"
    # initialize an empty node
    prev = None
    # create a temp reference to head
    current = head
    while(current!=None):
        # keep a reference to the node next to the current as it is the connection of current node to the rest of the linked list.
        currentPlusOne = current.next
        # change the direction of current node next to prev
        current.next = prev
        # after each iteration, we need to move the references towards the right side.
        # save the current to prev
        prev = current
        # save the next node to current node.
        current = currentPlusOne
    # head has changed to prev after the iteration is done
    head = prev
    return head


def printList(head: Node) -> Node:
    "print a linked list elements"
    temp = head
    while(temp!=None):
        print(temp.key, end =" ")
        temp = temp.next
        
    return temp
        
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("Original linked list")
printList(head)


newList = reverseLinkedList(head)
print("\nReversed linked list")
printList(newList)
