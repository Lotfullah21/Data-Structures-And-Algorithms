class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def insertAtPosition(head, pos, data):
    if head is None:
        return None
    
    # Create a new node with the given data
    new_node = Node(data)

    # Traverse to the node at position pos - 1
    current = head
    for _ in range(pos - 1):
        current = current.next
        if current == head:
            # If we have looped through the entire list,
            # the given position is greater than the size of the list
            return head

    # Insert the new node after the current node
    new_node.next = current.next
    current.next = new_node

    return head