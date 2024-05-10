class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
def displayList(head):
    curr = head
    result = []
    while curr!=None:
        result.append(curr.data)
        curr = curr.next
    return result

def isIdentical(head1, head2):
    "Returns True if two linked lists are identical"
    curr1 = head1
    curr2 = head2
    while curr1 is not None and curr2 is not None:
        # If one single of the node's data does not match, return False.
        if curr1.data!=curr2.data:
            return False
        curr2 = curr2.next
        curr1 = curr1.next
    # If both of the linked lists are traversed completely.
    if curr1 is None and curr2 is None:
        return True
    return False
    
head = Node(10)
head1 = Node(10)
head2 = Node(30)
head3 = Node(30)
head.next = head1
head1.next = head2
head2.next = head3


temp = Node(10)
temp1 = Node(10)
temp2 = Node(30)
temp3 = Node(30)
temp.next = temp1
temp1.next = temp2
temp2.next = temp3

print("First linked list")
linkedList = displayList(head)
for ele in linkedList:
    print(ele, end=">")
print()

print("Second linked list")
secondLinkedList = displayList(temp)
for ele in secondLinkedList:
    print(ele, end=">")
print()

same = isIdentical(head, temp)
print(same)
if same:
    print("two linked lists are identical")
else:
    print("they are not identical")
