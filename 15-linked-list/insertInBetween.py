class Node:
    def __init__(self, k):
        self.key = k 
        self.next = None
        
temp = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp4 = Node(1800)
temp.next = temp2
temp2.next = temp3
temp3.next = temp4

def insertIn(Node: Node,head:None, k: int, val: int) -> Node:
    "insert a node after kth node"
    temp = head
    kthNode = Node(val)
    for i in range(1, k):
        temp = temp.next
    # to keep the pointer of kth+1 node as we are breaking the bode in temp.next = kthNode.
    kthPlusOne = temp.next
    temp.next = kthNode
    # update the newly added next to saved pointer kthPlusOne .
    kthNode.next = kthPlusOne


def displayList(head: Node) -> Node:
    "display the current nodes in the linked list."
    curr = head
    # curr means, curr.next.
    while(curr!= None):
        print(curr.key, end=" ")
        # update the current, which is the next pointer.
        curr = curr.next
        
insertIn(Node, temp, 3, 90)
displayList(temp)