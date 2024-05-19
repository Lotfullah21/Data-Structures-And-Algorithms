## Question:

Given a linked list of length n, insert an element after given position. If the position is greater than n, do nothing.

Input: 1>2>5>6>7>-1
Position: 2
element:100
Output:1>2>5>100>6>7>-1
Explanation: The element 100 is inserted after 2nd's position.

##### 2nd Scenario:

Input: 1>2>5>6>7>-1
Position: 8
element:100
Output: 1>2>5>6>7>-1
Explanation: length of the linked list is 6 and the given position is 8, hence does not change the linked list.

### Analysis:

`Time Complexity`: `O(n)` We need to traverse the linked list to reach up to kth position or at worst case till the end.
`Space Complexity`: `O(1)`, Not using extra space, the result list is part of the output and does not count as extra space.
