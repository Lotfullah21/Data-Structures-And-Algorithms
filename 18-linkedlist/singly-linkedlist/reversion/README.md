## Reverse a linked list

Given a linked list of length n, reverse the linked list.

Input: 1>2>3>4>5>6
Output: 6>5>4>3>2>1

Input:1
Output:1

## Idea-1 (Using Stack)

### Algorithm:

- Create a stack.
- In first loop
  - At each iteration
  - Add the key to the stack until all element's keys are added.
- In second loop
  - At each iteration
  - Pop each element from the stack and replace it with the current keys.

```py

def reverseLinkedList(head: Node) -> list:
    """Reverses a linked list

    Args:
        head (Node): The head node

    Returns:
        list: A reversed linked list
    """
    if head is None:
        return None
    if head.next is None:
        return head
    else:
        current = head
        stack = []
        while current!=None:
            stack.append(current.key)
            current = current.next
        current = head
        while current!=None:
            current.key = stack.pop()
            current = current.next
    return head

```

## Analysis:

`Time Complexity`: `O(2*N)=O(N)`, because we are traversing the linked list twice, ignoring the constant it becomes O(N).

`Space Complexity`: `O(N)`, due to auxiliary stack space we are using to store the keys.

## Idea-2:

Do not change the data, change the link direction.

- Initialize two variables current and prev to head and None respectively.
- Traverse the linked list until you reached the end and at each iteration:
  - Save a pointer to the next of current.(nextNode = curr.next)
  - Change the next of current to be the prev.(curr.next = prev)
  - Change the prev to be current node. (prev = curr)
  - Change the current to be next of current you save at step-1.(curr = nextNode)

### Algorithm:

```py
def reverseLinkedList(head: Node) -> list:
    """Reverses a linked list

    Args:
        head (Node): The head node

    Returns:
        list: A reversed linked list
    """
    if head is None:
        return None
    if head.next is None:
        return head
    curr = head
    prev = None
    while curr!=None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev
```

## Analysis:

`Time Complexity`: `O(N)`, because we are traversing the linked list till the end.

`Space Complexity`: `O(1)`, No auxiliary space used.

It can be observed that the first method is using extra space and the second does not use any extra space.
