class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
            
def findMiddle(head):
    count = 0
    curr = head
    if head==None:
        return
    while curr != None:
        curr = curr.next
        count = count + 1
    curr = head
    for _ in range(0, count//2):
        curr = curr.next
    print(curr.data)    

def displayList(head: Node):
    "displays elements of a linked list"
    temp = head
    while(temp!=None):
        print(temp.data, end=" ")
        temp = temp.next
        
def findMiddleTwoPointer(head):
    if head==None:
        return
    slow = head
    fast = head
    # fast!=None is crucial, otherwise we will get NoneType has no attribute to next
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)  
          
def displayList(head: Node):
    "displays elements of a linked list"
    temp = head
    while(temp!=None):
        print(temp.data, end=" ")
        temp = temp.next
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)
temp4 = Node(40)
head.next = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
print("Original linked list: ",end=" ")
displayList(head)
print("\nLinked list after inserting a node in sorted linked list")
findMiddle(head)
findMiddleTwoPointer(head)