### Question:

Given a singly linked list of N elements, and element x, find if x is present in the linked list or not.

linkedList: 2>3>5>5
element: 3
Output: True

linkedList: 2>3>5>5
element: 1
Output: False

Explanation: 3 is present in the linked list and 1 is not.

Node Template:

```py

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

```

#### Idea

Traverse the whole linked list, if element is present, return `True`.
After reaching to the end of the linked list and still element x is not found, return `False` .

### Analysis:

`Time Complexity`: `O(n)` We need to traverse the list till the answer found or at the worst case, whole linked list should be searched.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
