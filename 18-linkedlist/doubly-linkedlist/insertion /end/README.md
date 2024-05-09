## Question:

Given a lined list with n nodes and a value x, insert x at the end of the linked list.

input:1>3>4>0>9
x=2
output:1>3>4>0>9>2

# Idea:

Basically, there are two approaches to solve this question,

## Idea-1:

Traverse the whole linked list and add x at the end.

```py

def insertInTail(head,data) -> list:
    newNode = Node(data)
    if head is None:
        return newNode
    curr = head
    # Traverse you hit the last node.
    while curr.next!=None:
        curr = curr.next
    # Save the last node
    tailNode = curr
    curr.next = newNode
    newNode.prev = tailNode
```

### Analysis:

`Time Complexity`: `O(n)`, Because of traversing the whole linked list.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.

## Idea-2:

Keep a reference for both: head and tail and append x after the tail.

### Analysis:

`Time Complexity`: `O(1)`, Just adding an element at the end and because of the tail reference, we do not need to traverse whole array.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertInTail(self, data):
        """Inserts a new node at the end of the linked list.

        Args:
            data (number): The value for the data field of the new node.
        """
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def displayList(self):
        """Returns a list containing the data field of each node in the linked list."""
        curr = self.head
        result = []
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

# Example usage
linkedList = LinkedList()
linkedList.insertInTail(0)
linkedList.insertInTail(20)
linkedList.insertInTail(30)
linkedList.insertInTail(40)
print("linked list =", linkedList.displayList())


```
