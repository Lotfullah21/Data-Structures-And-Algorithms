class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

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
insertInTail(head, 10)
insertInTail(head, 10)
insertInTail(head, 10)
insertInTail(head, 10)
insertInTail(head, 10)
insertInTail(head, 10)
ans = displayList(head)
print(ans)