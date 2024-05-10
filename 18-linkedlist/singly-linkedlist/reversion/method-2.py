class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def reverseLinkedList(head: Node) -> list:
    """Reverses a linked list 

    Args:
        head (Node): The head node

    Returns:
        list: A reversed linked list
    """
    if head is None:
        return None
    if head.next is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev            

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
