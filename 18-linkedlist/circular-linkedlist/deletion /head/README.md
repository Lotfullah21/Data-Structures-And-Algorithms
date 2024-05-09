## Delete head of a circular linked list

Given a circular linked list of length n, delete the head node.

input: 2>10>12>14
output: 10>12>14

Explanation: 2 is the head node and it got deleted.

### Idea-1:

Traverse the linked list and make the head of last node to be head.next

```py
def deleteHead(head):
    "Delete head of a node at constant time."
    if head is None:
        return None
    # Only one node in the list
    if head.next is head:
        return None
    current = head
    while current.next != head:
        current = current.next
    # Change the tail of last node to the next of head node.
    current.next = head.next
    return current.next


```

## Analysis:

`Time Complexity`: `O(n)`, We need to traverse the whole linked list.

### Idea-2(Optimal):

Use swapping operation.

#### Algorithm:

- Swap the data of current head and the node next to head.
- Break the chain of head to its next element and make next of head to be next of next of head(head.next.next)

```py
def deleteHead(head):
    if head is None or head.next is None:
        return None
    else:
        # Swap the values
        head.data = head.next.data
        # Break the chain.
        head.next = head.next.next
    return head

```

## Analysis:

`Time Complexity`: `O(1)`, We are just performing the swapping operation.
