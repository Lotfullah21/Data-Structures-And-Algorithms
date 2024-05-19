class Node:
    def __init__(self, k):
        self.key = k 
        self.next = None


def insertAtPosition(head: Node,pos: int,data: Node) -> list:
    """Inserts a node with value data after given position

    Args:
        head (Node): head of the linked list.
        pos (int): The position that after this, the new node should be added.
        data (Node): The value of new Node.

    Returns:
        Node: A new linked list with the given node added after kth position.
    """
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
                # If position is beyond the length of the linked list, return head and does not change anything.
                if temp.next is None:
                    return head
                # Iterate until you hit the position.
                temp = temp.next
            # Keep a pointer to the node after kth position.
            kthNodePlusOne = temp.next
            # Update the kth's next node to be new node
            temp.next = newNode
            # Update the new node next to be prev kth+1 node.
            newNode.next = kthNodePlusOne
    return head


def displayList(head: Node) -> Node:
    "display the current nodes in the linked list."
    curr = head
    linkedListData = []
    # curr means, curr.next.
    while(curr!= None):
        linkedListData.append(curr.key)
        curr = curr.next
    return linkedListData
     
        
head_node = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp4 = Node(1800)
head_node.next = temp2
temp2.next = temp3
temp3.next = temp4
   
head_node = insertAtPosition(head_node, 2, 90)
head_node = insertAtPosition(head_node, 0, 1)
head_node = insertAtPosition(head_node, 3, 190)
linkedList = displayList(head_node)
print("Linked list =", linkedList)