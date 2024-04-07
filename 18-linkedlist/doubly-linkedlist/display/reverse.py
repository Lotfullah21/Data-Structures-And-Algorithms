class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def displayList(head):
    if head is None:
        return
    forward_list = []
    curr = head
    while curr is not None:
        forward_list.append(curr.data)
        curr = curr.next
        if curr == head:  # Exit loop when we reach back to head
            break
    
    for ele in forward_list:
        print(ele, end=" ")
    print()  
    for i in range(len(forward_list)-1, -1, -1):
        print(forward_list[i],end=" ")

        

# Creating a circular doubly linked list
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)

head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
temp2.next = temp3
temp3.prev = temp2

# Call the displayList function
displayList(head)
