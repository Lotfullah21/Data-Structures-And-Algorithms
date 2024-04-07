class Node:
    def __init__(self, data):
         self.data = data
         self.next = None
         self.prev = None
         
def insertInTail(head,data):
    temp = Node(data)
    if head is None:
        return temp
    else:
        curr = head
        while curr.next!=None:
            curr = curr.next
        curr.next = temp
        temp.prev = curr
        return head
        
def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next 
         
head = None
head = insertInTail(head, 0)
head = insertInTail(head, 20)
head = insertInTail(head, 30)
head = insertInTail(head, 40)
printList(head)
