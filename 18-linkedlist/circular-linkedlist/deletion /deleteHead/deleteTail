class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def deleteTail(head):
    if head is None or head.next is head:
        # If the list is empty or has only one node, return None
        return None
    
    # Traverse to the second-to-last node
    current = head
    while current.next.next != head:
        current = current.next
    
    # Update the second-to-last node's next pointer
    current.next = head
    
    return head