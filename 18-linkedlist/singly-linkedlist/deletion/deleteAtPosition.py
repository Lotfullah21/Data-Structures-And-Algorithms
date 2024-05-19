class Node:
    def __init__(self, value):
        self.key = value
        self.next = None
        
def printList(head: Node) -> Node:
    curr = head
    while (curr!=None):
        print(curr.key, end=" ")
        curr = curr.next
# we do not have access to the hear here, just a pointer to the node to be deleted.
def deleteAtPosition(head: Node, pos: int) -> Node:
    "takes an integer as position to the node to be deleted and returns a modified linked list"
    #code here
    if head is None:
        return None
    elif pos == 1:
        head = head.next
        return head
    else:
        count = 1
        curr = head
        prev = None
        while curr is not None and count<pos:
            prev = curr
            curr = curr.next
            count+=1
        if curr is None:
            return head
        prev.next = curr.next
        return head

head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("Original linked list: ",end=" ")
printList(head)
head = deleteAtPosition(head,3)
print("\nLinked list after deleting the element at specified position: ",end =" ")
printList(head)