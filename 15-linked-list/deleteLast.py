class Node:
    def __init__(self, value):
        self.key = value
        self.next = None
        
def printList(head: Node) -> Node:
    curr = head
    while (curr!=None):
        print(curr.key, end=" ")
        curr = curr.next
        
def deleteLastNode(head: Node) -> Node:
    if head is not None and head.next is not None:
        # Here, temp and head are both references pointing to the same linked list. 
        # we use to temp to traverse. what changes happened caused by this will be reflected in original linkedList (head)
        temp = head
        # the 2nd last is node the one that 2ndLast.next.next == None.
        while(temp.next.next!=None):
            temp = temp.next
        # once found the 2nd last, cut the tail and put the next to the none value instead of last.
        temp.next = None
        # return the updated head
        return head
    print("HEAD IS NULL")

head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("Original linked list: ", end=" ")
printList(head)
newList = deleteLastNode(head)
print("\nLinked list after deleting the last node: ",end=" ")
printList(newList)