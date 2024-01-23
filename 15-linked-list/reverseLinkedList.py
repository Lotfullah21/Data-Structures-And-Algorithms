"""
Problem statement: Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.

"""



class Node:
    def __init__(self, val):
        self.key = val
        self.next = None
        
    
def reverseList(head):
    # initialize an empty node, because it will be assigned to first node and which will eventually becomes last node and last node always should be None.
    prev = None
    # create a temp reference to head
    current = head
    while(current!=None):
            # keep a reference to the node next to the current as it is the connection of current node to the rest of the linked list.
        currentPlusOne = current.next
            # change the link of current to prev node
        current.next = prev
            # after each iteration, we need to move the references towards the right side.
            # save the current to prev
        prev = current
            # move current one step to the right, save the next node to current node.
        current = currentPlusOne
        # head has changed to prev after the iteration is done, because based on termination condition, curr will be none and prev will
        # will be the last node, crucial to do this assignment.
    head = prev
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


newList = reverseList(head)
print("Reversed linked list")
printList(newList)
