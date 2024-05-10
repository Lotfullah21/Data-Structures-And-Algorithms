class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def reverseLinkedList(head: Node) -> Node:
    """Reverses a linked list 

    Args:
        head (Node): The head node

    Returns:
        Node: The head of the reversed linked list
    """
    if head is None:
        return None
    if head.next is None:
        return head
    else:
        curr = head
        stack = []
        while curr is not None:
            stack.append(curr.data)
            curr = curr.next
        curr = head
        while curr is not None:
            curr.data = stack.pop()
            curr = curr.next
    return head

# Function to print linked list
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original Linked List:")
printLinkedList(head)

# Reverse the linked list
reversed_head = reverseLinkedList(head)

print("Reversed Linked List:")
printLinkedList(reversed_head)
