class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def addNode(head, p, data):
    """Adds a new node with the given data at the specified position in the linked list.

    Args:
        head (Node): The head reference of the linked list.
        p (int): The position where the new node should be inserted (0-indexed).
        data: The value for the data field of the new node.

    Returns:
        Node: The head reference of the updated linked list.
    """
    newNode = Node(data)
    if head is None:
        return newNode
    if p <= 0:
        newNode.next = head
        head.prev = newNode
        return newNode
    curr = head
    for _ in range(p - 1):
        if curr.next is None:
            break
        curr = curr.next
    nextNode = curr.next
    curr.next = newNode
    newNode.prev = curr
    if nextNode:
        nextNode.prev = newNode
        newNode.next = nextNode
    return head

def displayList(head: Node) -> list:
    """Returns a list containing the data field of each node in the linked list starting from the given head.

    Args:
        head (Node): The head reference of the linked list.

    Returns:
        list: A list containing the data field of each node in the linked list.
    """
    curr = head
    result = []
    while curr is not None:
        result.append(curr.data)
        curr = curr.next
    return result

# Example usage
head = Node(120)
head = addNode(head, 0, 4)
head = addNode(head, 1, 12)
head = addNode(head, 2, 8)
head = addNode(head, 3, 20)
head = addNode(head, 2, 20)

ans = displayList(head)
print(ans)  # Output: [4, 120, 12, 20, 8, 20]
