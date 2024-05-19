# Stack Implementation using `deque` Collections

This code snippet demonstrates the implementation of a stack data structure using Python's `deque` collection from the `collections` module.

### Usage:

```python
from collections import deque

stack = deque()
stack.append(1)  # Adds 1 to the top of the stack
stack.append(2)  # Adds 2 to the top of the stack
stack.append(3)  # Adds 3 to the top of the stack
stack.append(4)  # Adds 4 to the top of the stack
stack.append(5)  # Adds 5 to the top of the stack

def isEmpty(stack: deque) -> bool:
    "Checks if the deque is empty or not."
    if stack:
        return False
    return True

print("Stack:", stack)

size = len(stack)
print("Size of Stack:", size)

isEmpty = isEmpty(stack)
print("Is Stack Empty:", isEmpty)

top = stack[-1]
print("Top of Stack:", top)

stack.pop()   # Removes the last element from the stack
stack.pop()   # Removes the last element from the stack
stack.pop()   # Removes the last element from the stack

print("Updated Stack:", stack)
```
