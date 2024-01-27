"""Implementing a stack using deque collections"""
from collections import deque

stack = deque()
stack.append(1) # add 1  to the top of the stack
stack.append(2)  # add 2 to the top of the stack
stack.append(3)   # add 3 to the top of the stack
stack.append(4)   # add an 4 to the top of the stack
stack.append(5)   # add an 5 to the top of the stack

def isEmpty(stack: list) -> bool:
    "checks if the list is empty or not."
    if stack:
        return False
    return True

print("stack",stack)
size = len(stack)
print("size",size)

isEmpty = isEmpty(stack)
print("isEmpty",isEmpty)

top = stack[-1]
print("top",top)

stack.pop()  # removes last elem in list
stack.pop() # removes last elem in list
stack.pop()  # removes last elem in list
print(stack)