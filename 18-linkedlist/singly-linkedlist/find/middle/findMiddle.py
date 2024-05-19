class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
            

def findMid(head):
    if head is None:
        return None
    fast = head
    slow = head
    while fast!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
    return slow.data
        


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
temp4 = Node(50)
head.next = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4

linkedList = displayList(head)
for ele in linkedList:
    print(ele, end=">")
print()

midElement = findMid(head)
print("Middle element =", midElement)