class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def printList(head: Node) -> int:
    "Prints present nodes in a linked list."
    if head == None:
        return 
    print(head.data,end=" ")
    current = head.next
    while current!=head:
        print(current.data,end=" ")
        current = current.next
    print()
            
def getLength(head: Node) -> int:
    "Returns number of elements in a linked list"
    linkedList = []
    if head == None:
        return 
    linkedList.append(head.data)
    current = head.next
    while current!=head:
        linkedList.append(current.data)
        current = current.next
    return len(linkedList)

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
printList(head)
length = getLength(head)
print(length)