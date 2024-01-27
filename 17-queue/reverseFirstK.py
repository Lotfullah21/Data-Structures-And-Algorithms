from collections import deque
queue = deque()
stack = deque()
elements = [1,2,3,4,5,6,7,8,9]
n = len(elements)
print("len =",n)
for i in range(len(elements)):
        queue.append(elements[i])
def reverseFirstK(k: int) -> deque:
    "reverse first k integers in a queue"
    for _ in range(k):
        stack.append(queue.popleft())
    for _ in range(k):
        queue.append(stack.pop())
    print(queue)
    for _ in range(n-k):
        queue.append(queue.popleft())
    print(queue)
    
reverseFirstK(3)