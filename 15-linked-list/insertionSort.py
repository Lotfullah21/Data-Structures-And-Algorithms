class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
            
def displayList(head: Node):
    "displays elements of a linked list"
    temp = head
    while(temp!=None):
        print(temp.data, end=" ")
        temp = temp.next
        
def insertInSorted(head: Node, ele: int) -> Node:
    "takes an integer and compare it with other node's data, if it is smaller than head, inserts it at the beginning, else, it will traverse until meet the condition."
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
        # because we are changing head in above two if and elif conditions, we need to return head
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
print("\nLinked list after inserting a node in sorted linked list: ",end =" ")
displayList(head)