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
        
def displayList(head: Node) -> None:
    "Prints present nodes in a linked list."
    result = []
    current = head
    result.append(current.data)
    current = head.next
    while current != head:
        result.append(current.data)
        current = current.next
    return result

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
newHead = deleteHead(head)
ans  = displayList(newHead)
print("Linked list after head deletion", ans)