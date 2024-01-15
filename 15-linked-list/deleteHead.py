class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        
def printList(head):
    curr = head
    while(curr!=None):
        print(curr.key, end = " ")
        curr = curr.next

def deleteHead(head: Node) -> Node:
    if head is not None:
        head = head.next
    return head
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("original linked list")
printList(head)
head = deleteHead(head)
print("\n linked list after deleting the head")
printList(head)