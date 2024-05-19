class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
def insertInMid(head,node):
    newNode = Node(node)
    # handling the case if list is empty.
    if head==None:
        head = node
        return head
    # pointers.
    slow = head
    fast = head 
    # fast.next.next to keep the pointer one step behind the mid, because we want to replace mid.
    while fast!=None and fast.next!=None and fast.next.next!=None:
        slow = slow.next
        fast = fast.next.next
    next = slow.next
    slow.next = newNode
    newNode.next = next
    return head

def displayList(head: Node) -> Node:
    "Returns a linked list' sta"
    temp = head
    result  = []
    while(temp!=None):
        result.append(temp.data)
        temp = temp.next
    return result
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("Original linked list")
linkedList = displayList(head)
for ele in linkedList:
    print(ele, end=">")
print()
element = 90
newList = insertInMid(head,element)
print("New linked list after inserting",element,"in mid")
linkedList = displayList(head)
for ele in linkedList:
    print(ele, end=">")
print()