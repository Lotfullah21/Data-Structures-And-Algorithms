class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None


def deleteHead(head: Node) -> Node:
    "Deletes the head of the node and returns a new head."
    # If no element is present at all.
    if head is None:
        return None
    # If there is only one node
    if head.next is None:
        return None
    curr = head
    # Break the chain of head to its next element and make it new head.
    head = curr.next
    head.prev = curr.prev
    return head


def insertInTail(head,data):
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
print("linked list before deletion of head node=",ans)
newList = deleteHead(head)
ans = displayList(newList)
print("linked list after deletion of head node=",ans)

