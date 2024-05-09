class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
            
def insertInHead(head, x):
    "Insert Node x in the beginning in constant time"
    newNode = Node(x)
    if head is None:
        newNode.next = newNode
        return newNode
    # Make the new node, next of head.
    nextNode = head.next
    head.next = newNode
    newNode.next = nextNode
    # Swap the value.
    temp = head.data
    head.data = newNode.data
    newNode.data = temp
    return head
    
    

def printList(head: Node) -> int:
    "Prints present nodes in a linked list."
    if head == None:
        return 
    result = []
    result.append(head.data)
    current = head.next
    while current.next!=head:
        result.append(current.data)
        current = current.next
    return result


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
insertInHead(head, 0)
insertInHead(head, 100)
linkedList = printList(head)
print("Linked list after insertion in the head",linkedList)