class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
        
def insertAtBegin(head, ele):    
    node = Node(ele)
    node.next = head
    return node

def display(head):
    res = []
    curr = head
    while curr!=None:
        res.append(curr.key)
        curr = curr.next
    return res
        
        

        
head = Node(10)
temp2 = Node(20)
temp3 = Node(30)


head.next = temp2
temp2.next = temp3
temp3.next = None

answer = display(head)
print(answer)
result = insertAtBegin(head,90)
result = insertAtBegin(result,-1)
answer = display(result)
print(answer)