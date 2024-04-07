class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

def addNode(head, p, data):
    temp = Node(data)
    if head is None:
        return temp
    if p==0:
        curr = head
        nextNode = curr.next
        curr.next = temp
        temp.next = nextNode
        temp.prev = head
    else:
        curr = head
        for i in range(p):
            curr = curr.next
        prevNode = curr.prev
        nextNode = curr.next
        curr.next = temp
        temp.prev = prevNode
        temp.next = nextNode
        
        