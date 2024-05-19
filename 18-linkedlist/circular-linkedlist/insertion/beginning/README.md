## Insert in the beginning:

Given a circular linked list of length n, insert an element in head of the linked list.

Input: 1>2>3>4>5.
Element: 0.
Output: 0>1>2>3>4>5.

### Idea-1 (Brute force):

Because of its circular nature, head cannot be simply added like singly linked list.

#### Algorithm:

- Traverse the whole array
- Update next of tail to be the new node.
- Update next of new node to be previous head.

```py

def insertInHead(head, x):
    current = head
    newNode = Node(x)
    while current.next!=head:
        current = current.next
    current.next = newNode
    newNode.next = head
    head = newNode
    return head
```

### Analysis:

`Time Complexity`: `O(n)` We need to traverse the linked list to reach to the last node.

## Idea-2 (Optimal):

- Create a newNode for the element to be inserted.
- Make next of head to be newNode.
- Swap there values.

```py

def insertInHead(head, x):
    "Insert Node x in the beginning in constant time"
    newNode = Node(x)
    if head is None:
        head = newNode
        return head
    # Make the new node, next of head.
    nextNode = head.next
    head.next = newNode
    newNode.next = nextNode
    # Swap the value.
    temp = head.data
    head.data = newNode.data
    newNode.data = temp
    return head

```

### Analysis:

`Time Complexity`: `O(1)`, Because we are just swapping the values of head node and the new node.
