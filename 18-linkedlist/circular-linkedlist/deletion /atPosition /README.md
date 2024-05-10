## Question:

Given a linked list of length n, delete a node at given position k.
it is 1th based indexing.

input: 2>10>12>14
k = 1
output: 10>12>14

input: 2>10>12>14
k = 3
output: 2>10>14

## Idea:

- Traverse the linked up to one node before kth node.
- Change the next of that node to be next of next (node.next.next).
- As indexing is one based indexing, run the loop for (K-2) times.
- Return head

Handle the case when k==0 or k==1 explicitly.

```py
def deleteKthNode(head, k):
    "Deletes Kth node in a linked list"
    if head is None:
        return None
    elif k==1:
        return deleteHead(head)
    current = head
    for _ in range(k-2):
        current = current.next
    current.next = current.next.next
    return head

```
