from collections import deque

dq = deque()
def push_front_pf(dq,x):
    dq.appendleft(x)
    

#Function to push element x to the back of the deque.
def push_back_pb(dq,x):
    dq.append(x)
    
#Function to return element from front of the deque.
def front_dq(dq):
    if not dq: return -1
    return dq[0]
    
#Function to pop element from back of the deque.
def pop_back_ppb(dq):
    if dq:
        dq.pop()
# Creating an empty deque


# Adding elements to the deque using the provided functions
push_back_pb(dq, 10)
push_front_pf(dq, 5)
push_back_pb(dq, 20)

# Getting the element at the front of the deque
print(front_dq(dq))  # Output: 5

# Removing the element at the back of the deque
pop_back_ppb(dq)

# Getting the element at the front of the deque after removal
print(front_dq(dq))  # Output: 5

# Printing the deque
print(dq)  # Output: deque([5, 10])
