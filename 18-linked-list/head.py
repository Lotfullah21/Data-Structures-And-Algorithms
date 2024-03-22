class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def printList(head):
        curr = head
        while(curr!=None):
            print(head.key,end=" ")
            curr = curr.next
        


def printList(head: Node) -> list:
    curr = head
    while(curr!=None):
        print(curr.key,end=" ")
        curr = curr.next
# using list
def displayList(head: Node) -> list:
    result = []
    temp = head
    while(temp!=None):
        result.append(temp.key)
        temp = temp.next
    return result


        
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp1.next = temp2
temp2.next = temp3
printList(temp1)
new_list = displayList(temp1)
print("Using list")
for ele in new_list:
    print(ele, end=" ")