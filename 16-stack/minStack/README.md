### Question:

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

### Idea

Use a single stack to keep the gaps between the min element and current element.

#### Analysis:

`Time Complexity` is `O(1)`, for each operation.
`Space Complexity` is `O(1)`, just one single stack space.
