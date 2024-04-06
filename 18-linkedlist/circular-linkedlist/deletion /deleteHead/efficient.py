class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def DeleteTail(head):
    "Delete head of a node at constant time."
    if head is None:
        return None
    # Only one node in the list
    if head.next is head:  
        return None
    # Copy the data next to head to current head, and connect the current head with next to the next of head.
    head.data = head.next.data
    head.next = head.next.next
    return head

        
def printList(head: Node) -> None:
    "Prints present nodes in a linked list."
    if head is None:
        return 
    print(head.data, end=" ")
    current = head.next
    while current != head:
        print(current.data, end=" ")
        current = current.next
        if current == head:
            break
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
head = DeleteTail(head)
printList(head)
