class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
        
def displayList(head):
    temp = head
    while(temp!=None):
        print(temp.data, end=" ")
        temp = temp.next
        
def insertInSorted(head, ele):
    newNode = Node(ele)
    if head==None:
        head = newNode
        return head
    elif head.data >ele:
        newNode.next = head
        head = newNode
        return head
    else:
        temp = head
        # take care of conditions, which one to put first.
        while temp.next!=None and temp.next.data<ele:
            temp = temp.next
        plusOneNode = temp.next
        temp.next = newNode
        newNode.next = plusOneNode
        return head
        
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)



head.next = temp1
temp1.next = temp2
temp2.next = temp3
print("Original linked list: ",end=" ")
displayList(head)
head = insertInSorted(head,390)
print("\nLinked list after deleting the element at specified position: ",end =" ")
displayList(head)