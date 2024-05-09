## Question:

Given a doubly linked list, delete its tail node.

input: 2<-->4<-->6<-->8<-->10<-->12<-->14.
output: 2<-->4<-->6<-->8<-->10<-->12.

Explanation: tail node here is 14 and after removal, it should not appear in the linked list.

input: 2.
output: None.
Explanation: Only one node is present, after removal of 2, no node is remained in the linked list.

## Hint:

Traverse the whole linked list, cut the chain from the 2nd last node and make it None.

### Analysis:

`Time Complexity`: `O(n)`, Because of traversing the whole linked list.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
