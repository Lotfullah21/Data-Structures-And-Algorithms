## Question:

Given an array of numbers, write a function that takes two parameters: the head none and an element to be inserted at the beginning.
return a new list that contains the list with given element inserted at the beginning.

input: 2>3>5>9>-1
element = -12
output: -12>2>3>5>9>-1

### Analysis:

`Time Complexity`: `O(1)`, Just adding an element at the beginning does not require to travel the whole array.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
