from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        n = len(self.q)
        # iterate until last element.
        for _ in range(n - 1):
            # add element up to n-1th to the end of the q.
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.top())  # Output: 4
print(stack.pop())  # Output: 4
