class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
  
def addNode(head, p, data):
    # Code here
    newNode = Node(data)
    if head is None:
        head = newNode
        return head
    elif p==0:
        curr = head
        nextNode = curr.next
        curr.next = newNode
        newNode.next = nextNode
        newNode.prev = curr
        return newNode
    else:
        curr = head
        for i in range(p):
            curr = curr.next
        nextNode = curr.next
        prevNode = curr.prev
        curr.next = newNode
        newNode.prev = prevNode
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
p = 0
data = 20
adAtKth = addNode(head, p, data)
adAtKth = addNode(head, 1, 12)
adAtKth = addNode(head, 3, 20)
adAtKth = addNode(head, 2, 8)
adAtKth = addNode(head, 0, 4)

ans = displayList(head)
print(ans)