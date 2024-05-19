class Node:
    def __init__(self, data):
         self.data = data
         self.next = None
         self.prev = None
         
def insertBegin(head: Node, x) -> Node:
    """Inserts a new node at the beginning of the linked list.

    Args:
        head (Node): The starting reference of the linked list.
        x (number): The value for the data field of the new node.

    Returns:
        Node: The new head of the linked list.
    """
    temp = Node(x)
    if head is None:
        # If the linked list is empty, set the new node as the head and return it.
        temp.next = head
        return temp
    # If the linked list is not empty, insert the new node before the current head.
    temp.next = head
    # Only change the head's previous when head is not None.
    head.prev = temp
    # Update the head to the newly inserted node.
    return temp

        
        
        
def displayList(head: Node) -> list:
    """Returns a list containing the data field of each node in the linked list starting from the given head.

    Args:
        head (Node): The head reference of the linked list.

    Returns:
        list: A list containing the data field of each node in the linked list.
    """
    curr = head
    result = []
    while curr is not None:
        result.append(curr.data)
        curr = curr.next
    return result

         
         
head = None
head = insertBegin(head, 20)
head = insertBegin(head, 30)
head = insertBegin(head, 40)
linkedList = displayList(head)
print("linked list", linkedList)
