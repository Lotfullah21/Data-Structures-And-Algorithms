class Node:
    def __init__(self, data):
         self.data = data
         self.next = None
         self.prev = None
         
def insertBegin(head, x):
    temp = Node(x)
    if head is not None:
        head.prev = temp
    temp.next = head
    # Update the head to the newly inserted node
    return temp
        
def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next 
         
head = None
head = insertBegin(head, 20)
head = insertBegin(head, 30)
head = insertBegin(head, 40)
printList(head)
