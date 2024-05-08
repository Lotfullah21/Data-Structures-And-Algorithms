### Question:

Given a singly linked list, display the linked list data.

Input: 2>3>5>5

Output: 2 3 5 5

```py

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

```

### Idea:

Traverse the linked list until you hit the None which means we reached to the end of a linked list.
Use a while loop and at every iteration, move node one step a head towards the tail using next reference.

### Analysis:

`Time Complexity`: `O(n)` We need to traverse the whole linked list to reach to the end point.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
