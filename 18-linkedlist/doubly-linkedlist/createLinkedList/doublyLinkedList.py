class Node:
     def __init__(self, data):
         self.data = data
         self.next = None
         self.prev = None
         
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
temp2.next = temp3
temp3.prev = temp2