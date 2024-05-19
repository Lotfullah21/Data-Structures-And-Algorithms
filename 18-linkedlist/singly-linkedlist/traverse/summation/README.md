### Question:

Given a singly linked list of length n, sum the node's data and return it.

Input: 2>3>5>5

Output: 15

Explanation: 2+3+5+5=15

Node Template:

```py

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

```

### Idea:

Traverse the linked list until you hit the None which means we reached to the end of a linked list.
Use a while loop and at every iteration, move node one step a head towards the tail using next reference.
Add the node's data at each iteration to a variable defined before the loop.

### Analysis:

`Time Complexity`: `O(n)` We need to traverse the whole linked list to reach to the end point.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
