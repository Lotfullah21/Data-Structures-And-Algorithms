## Question:

Given a lined list with n nodes and a value x, insert x at the end of the linked list.

input:1>3>4>0>9
x=2
output:1>3>4>0>9>2

### Analysis:

`Time Complexity`: `O(1)`, Just adding an element at the beginning does not require to travel the whole array.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
