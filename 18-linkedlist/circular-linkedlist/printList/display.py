class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def displayList(head: Node) -> int:
    "Returns a list containing all linked list's data."
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
displayList(head)
length = getLength(head)
print(length)