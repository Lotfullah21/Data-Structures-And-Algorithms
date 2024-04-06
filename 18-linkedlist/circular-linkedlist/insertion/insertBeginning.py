class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def insertBeginning(head, x):
    "Insert at the head of node in linear time."
    temp = Node(x)
    if head==None:
        temp.next = None
        return temp
    current = head
    while current.next!=head:
        current = current.next
    current.next = temp
    temp.next = head
    return temp

    
def insertAtBeginning(head, x):
    "Insert Node x in the beginning in constant time"
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        temp.data, head.data = head.data, temp.data
        return head

def printList(head: Node) -> int:
    "Prints present nodes in a linked list."
    if head == None:
        return 
    print(head.data,end=" ")
    current = head.next
    while current.next!=head:
        print(current.data,end=" ")
        current = current.next
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
insertBeginning(head, 0)
insertAtBeginning(head, 100)
printList(head)