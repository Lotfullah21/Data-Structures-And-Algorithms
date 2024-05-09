## Question:

Given a linked list of length n, return the data of the linked list.

Input:`<2>4>6>8>10>`
Output: 2 4 6 8 10

## Idea-1:

Since, it is circular linked list, the end will be where the next of a node is the head node;Stop there.
To do so:

- Use a temporary variable
- Traverse the array using a loop until you reached a point where the next of a node is head(temp.next==head).
  - Inside the loop, add the current data to the list.
- After exiting the loop the, Add the last node data to the list.

```py
def displayList(head):
    #code here
    result = []
    current = head
    while current.next!=head:
        result.append(current.data)
        current = current.next
    result.append(current.data)
```

## Idea-2:

Since, it is circular linked list, the end will be where head is traversed twice.
To do so:

- Use a temporary variable
- Add the head's data to the list.
- Update the current to be next of head (head.next)
- Traverse the array using a loop until you reached a point where head is reached
  - Inside the loop, add the current data to the list.
- Exit the loop.

```py
def displayList(head: Node) -> int:
    "Prints present nodes in a linked list."
    if head == None:
        return
    result = []
    result.append(current)
    current = head.next
    while current!=head:
        result.append(current)
        current = current.next
    return result

```
