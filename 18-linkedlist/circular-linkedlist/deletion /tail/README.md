## Delete tail(last element)

Given a circular linked list, delete tail of the linked list.

input: 2>10>12>14
output: 2>10>12

Explanation: 4 is the tail node and it got deleted.

## Idea-1 (Brute Force):

### Algorithm:

- Traverse the linked before reaching the last node.
- Make the next of the node previous to tail node to be head.

```py
def deleteTail(head):
    #code here
    if head is None or head.next is None:
        return None
    current = head
    while current.next.next!=head:
        current = current.next
    current.next = current.next.next
    return head

```
