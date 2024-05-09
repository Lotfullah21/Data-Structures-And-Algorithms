class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def deleteHead(head):
    "Delete head of a node at constant time."
    if head is None:
        return None
    # Only one node in the list
    if head.next is head:  
        return None
    current = head
    while current.next != head:
        current = current.next
    # Change the tail of last node to the next of head node.
    current.next = head.next
    return current.next
        
def deleteKthNode(head, k):
    "Deletes Kth node in a linked list"
    if head is None:
        return None
    elif k==1:
        return deleteHead(head)
    current = head
    for i in range(k-2):
        current = current.next
    current.next = current.next.next
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
newHead = deleteKthNode(head, 2)
printList(head)
