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


# adding it manually
newNode = Node(-1)
# assign the next of newly Created node to the prev head.
newNode.next = head
# re-assign the head to the newly created node.
head = newNode


def printList(head: Node):
    "traverse through a lined list and print its values"
    curr = head
    while(curr!=None):
        print(curr.key,end=" ")
        curr = curr.next
        


# a function to do the above task
def insertionAtStart(node: Node, val: int,prevHead: vars) -> Node:
    "insert a node at the beginning of a node"
    newNode = node(val)
    newNode.next = prevHead
    prevHead = newNode
    printList(prevHead)
    

insertionAtStart(node = Node, val=10,prevHead = head )

print()
printList(head)