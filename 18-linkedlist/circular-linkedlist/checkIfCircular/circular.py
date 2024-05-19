class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def isCircular(head):
    # Start one step ahead of next node.
    curr = head.next
    # Iterate until the current becomes None or reach to head.
    while curr!=None and curr!=head:
        curr = curr.next
    if curr==head:
        return True
    else:
        return False

def isCircular(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while fast!=None and fast.next!=None:
        if fast==slow:
            return True
        fast = fast.next.next
        slow = slow.next




head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = head
newHead = isCircular(head)
print(newHead)