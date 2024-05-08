class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
                    
    
# using list
def displayList(head: Node) -> list:
    """Returns the linked list data

    Args:
        head (Node): head of a linked list

    Returns:
        list: list of node's data
    """
    result = []
    temp = head
    while(temp!=None):
        result.append(temp.data)
        temp = temp.next
    return result

def searchLinkedList(head: Node,x: int) -> int:
    "takes the head node and an integer as input, returns 1 if x is in linked list, -1 if not present"
    curr = head
    while curr!=None:
        if curr.data==x:
            return True
        curr = curr.next
    return False

head = Node(10)
temp2 = Node(20)
temp3 = Node(30)
head.next = temp2
temp2.next = temp3
element = 30
linkedlist = displayList(head)
print("linked list =", linkedlist)
result = searchLinkedList(head, element)
print("result =",result)