class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def deleteTail(head: Node) -> Node:
    "Deletes the last node from the linked list and return a new linked list."
    if head is None or head.next is None:
        return None
    curr = head
    # Iterate up to the last node
    while curr.next!=None:
        curr = curr.next
    # Find the previous to last node
    secondLastNode = curr.prev
    # Break the chain and make next of last 2nd node to None
    secondLastNode.next = None
    return head


def insertInTail(head,data):
    #code here
    newNode = Node(data)
    if head is None:
        head = newNode
        return head
    curr = head
    while curr.next!=None:
        curr = curr.next
    tailNode = curr
    curr.next = newNode
    newNode.prev = tailNode
    return head


def displayList(head: Node) -> list:
    """Returns a list containing the data field of each node in the linked list starting from the given head."""
    curr = head
    result = []
    while curr is not None:
        result.append(curr.data)
        curr = curr.next
    return result



# Example usage
head = Node(2)
insertInTail(head, 4)
insertInTail(head, 6)
insertInTail(head, 8)
insertInTail(head, 10)
insertInTail(head, 12)
insertInTail(head, 14)
ans = displayList(head)
print("Original linked list",ans)
newLinkedList = deleteTail(head)
ans = displayList(newLinkedList)
print("Linked list after tail's node deletion",ans )