class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
             
def printList(head: Node) -> None:
    """Prints a linked list

    Args:
        head (Node): head of a node

    Returns:
        list: None
    """
    curr = head
    while(curr!=None):
        print(curr.key,end=" ")
        curr = curr.next
    print()

        
# using list
def displayList(head: Node) -> list:
    "Returns values of a linked list"
    result = []
    temp = head
    while(temp!=None):
        result.append(temp.key)
        temp = temp.next
    return result


        
head = Node(10)
temp2 = Node(20)
temp3 = Node(30)
head.next = temp2
temp2.next = temp3
printList(head)
new_list = displayList(head)

print("Using list",end=" ")
for ele in new_list:
    print(ele, end=" ")
print()
