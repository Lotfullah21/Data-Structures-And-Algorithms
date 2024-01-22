class Node:
    def __init__(self,value):
        self.key = value
        self.next = None
        
n1 = Node(0)
n2 = Node(1)
n3 = Node(2)

head = n1
n1.next = n2
n2.next = n3

def printList(head: Node):
    "traverse through a lined list and print its values"
    curr = head
    while(curr!=None):
        print(curr.key,end=" ")
        curr = curr.next
        
# a function to do the above task
def insertionAtStart(node: Node, val: int,head: Node) -> Node:
    "insert a node at the beginning of a node"
    newNode = node(val)
    newNode.next = head
    return newNode
    
head = insertionAtStart(node = Node, val=3,head = head )
head = insertionAtStart(node = Node, val=4,head = head )
head = insertionAtStart(node = Node, val=5,head = head )
print("New linked list after inserting three elements")
# printList(head)
printList(head)
