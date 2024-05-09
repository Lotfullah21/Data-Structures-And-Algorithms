class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def insertAtTail(head: Node, x: int) -> Node:
    newNode = Node(x)
    if head is None:
        newNode.next = newNode
        return newNode
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = newNode
        newNode.next = head
        return head
    

def displayList(head: Node) -> int:
    "Prints present nodes in a linked list."
    if head == None:
        return 
    result = []
    current = head
    result.append(current.data)
    current = head.next
    while current!=head:
        result.append(current.data)
        current = current.next
    return result

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
newHead = insertAtTail(head, 40)
linkedList = displayList(newHead)
print(linkedList)