# Stack Implementation in Python

This is a basic implementation of a stack data structure in Python, using a list to simulate the stack behavior. The stack has a maximum size limit set to 10000 elements.

### Functions:

#### 1. `push(data)`

- Adds an element to the top of the stack.
- **Parameters**:
  - `data`: The value to be added to the stack.
- **Returns**: None
- **Behavior**:
  - Increments the `top` pointer to move to the next available position.
  - Checks if the stack is full (more than 10000 elements), prints "Stack Is Full" if true.
  - Otherwise, appends the `data` to the `stack`.

#### 2. `pop()`

- Removes the element from the top of the stack.
- **Parameters**: None
- **Returns**: None
- **Behavior**:
  - Checks if the stack is empty (when `top` is -1), prints "Stack Is Empty" if true.
  - Otherwise, removes the element at the `top` position in the `stack` and decrements `top`.

#### 3. `display()`

- Displays the elements of the stack.
- **Parameters**: None
- **Returns**: None
- **Behavior**:
  - Checks if the stack is empty (when `top` is -1), prints "-1" if true.
  - Otherwise, iterates through the `stack` from index 0 to `top` and prints each element.

### Global Variables:

- `stack`: The list representing the stack.
- `top`: The index of the top element in the stack. Initialized to -1.
- `stackMax`: The maximum allowed size of the stack, set to 10000.

### Example Usage:

```python
stack = []
top = -1
stackMax = 10000

push(10)
push(20)
push(10)
push(10)
display()
```
