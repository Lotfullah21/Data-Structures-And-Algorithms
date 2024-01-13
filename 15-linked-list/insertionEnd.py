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
    while(curr != None):
        print(curr.key,end=" ")
        curr = curr.next
        


# a function to do the above task
def insertionAtEnd(node: Node, val: int,prevHead: head) -> Node:
    "insert a node at the end of a node"
    
    temp = prevHead
    while(temp.next != None):
        temp = temp.next
    temp.next = node(val)
    printList(prevHead)
    

insertionAtEnd(node = Node, val=9,prevHead = head )

print()
printList(head)