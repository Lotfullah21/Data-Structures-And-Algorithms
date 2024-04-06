class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def insertAtTail(head: Node, x: int) -> Node:
    temp = Node(x)
    if head is None:
        temp.next = temp
        return temp
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = temp
        temp.next = head
        return head
    

def printList(head: Node) -> None:
    "Prints present nodes in a linked list."
    if head is None:
        return 
    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
newHead = insertAtTail(head, 40)
printList(newHead)
