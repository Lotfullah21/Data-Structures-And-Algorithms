class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
           
def summation(head: Node) -> int:
    """Returns sum of node's data

    Args:
        head (Node): head of the linked list

    Returns:
        int: results of node's data
    """
    result = 0
    curr = head
    while curr!=None:
        result = result + curr.data
        curr = curr.next
    return result
    
    
# Constructing the nodes.
head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(5)


answer = summation(head)
print("sum =",answer)