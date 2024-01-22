class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
    def printList(head):
        curr = head
        while(curr!=None):
            print(head.key,end=" ")
            curr = curr.next
# print the elements inside a linked list
def printList(head: Node) -> list:
    curr = head
    while(curr!=None):
        print(curr.key,end=" ")
        curr = curr.next

def searchLinkedList(head: Node,x: int) -> int:
    "takes the head node and an integer as input, returns 1 if x is in linked list, -1 if not present"
    #code here
    temp = head
    while temp!=None:
        if temp.data==x:
            return 1
        temp = temp.next
    return 0

head = Node(10)
temp2 = Node(20)
temp3 = Node(30)
head.next = temp2
temp2.next = temp3
element = 30
result = searchLinkedList(head, element)
print("result",result)