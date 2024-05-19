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
    
def removeDuplicates(head: Node) -> None:
    "Removes duplicate nodes if present in the linked list"
    curr = head
    result = []
    while curr!=None and curr.next!=None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
            
        
    
head = Node(10)
temp1 = Node(10)
temp2 = Node(30)
temp3 = Node(30)

head.next = temp1
temp1.next = temp2
temp2.next = temp3

print("Original linked list")
linkedList = displayList(head)
for ele in linkedList:
    print(ele, end=">")
print()

print("linked list after duplicates removal")
newLinkedList = removeDuplicates(head)
newLinkedList = displayList(newLinkedList)
for ele in newLinkedList:
    print(ele, end=">")
print()

