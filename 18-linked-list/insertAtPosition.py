class Node:
    def __init__(self, k):
        self.key = k 
        self.next = None
        
head_node = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp4 = Node(1800)
head_node.next = temp2
temp2.next = temp3
temp3.next = temp4

def insertAtPosition(head: Node,pos: int,data: Node) -> Node:
    "insert a node at kth position"
    if head is None:
        head = Node(data)
    else:
        newNode = Node(data)
        temp = head
        if pos==0:
            newNode.next = head
            # Now, new node becomes our head.
            return newNode
        else:
            for _ in range(1, pos):
                # if position is beyond the length of the linked list, return head and does not change anything.
                if temp.next is None:
                    return head
                temp = temp.next
            # keep a pointer to the node after kth position
            kthNodePlusOne = temp.next
            # update the kth next node to be new node
            temp.next = newNode
            # update the new node next to be prev kth+1 node.
            newNode.next = kthNodePlusOne
    return head

def displayList(head: Node) -> Node:
    "display the current nodes in the linked list."
    curr = head
    # curr means, curr.next.
    while(curr!= None):
        print(curr.key, end=" ")
        # update the current, which is the next pointer.
        curr = curr.next
        
head_node = insertAtPosition(head_node, 2, 90)
head_node = insertAtPosition(head_node, 0, 1)
head_node = insertAtPosition(head_node, 3, 190)
displayList(head_node)