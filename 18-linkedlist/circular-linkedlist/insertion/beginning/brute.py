class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def insertInHead(head, x):
    "Insert at the head of node in linear time."
    temp = Node(x)
    if head==None:
        temp.next = None
        return temp
    current = head
    while current.next!=head:
        current = current.next
    # Update the next of tail node
    current.next = temp
    # Update the next of inserted node to be previous head.
    temp.next = head
    # Temp becomes new head.
    return temp



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