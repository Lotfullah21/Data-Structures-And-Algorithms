## Stack:

it is a linear data structure that follows a particular order in which the operations are performed.
by linear we refer to a way of organizing and storing data elements where data elements are arranged in sequential manner.
This means that each element has a unique predecessor and successor, except for the first and last elements, respectively.

to do operations in these types of data structures, a specific order will be followed.

## Deque

deque implementation is based on doubly linked list, where we adding operations on the right of the linked list.
all the operation is done in O(1).

lists are cache friendly as the elements are stored in contiguous location and the worst time complexity is linear.
for deque, becaus individual references are at different locations, hence not cache friendly.
