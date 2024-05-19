class Node:
    def __init__(self, key):
        self.key = key
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
        result.append(temp.key)
        temp = temp.next
    return result


# Head node
head = Node(10)
temp2 = Node(20)
temp3 = Node(30)
head.next = temp2
temp2.next = temp3
new_list = displayList(head)

for ele in new_list:
    print(ele, end=" ")
print()
