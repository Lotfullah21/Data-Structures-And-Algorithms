## Stack:

It is a linear data structure that follows a particular order in which the operations are performed.
By linear we refer to a way of organizing and storing data elements where data elements are arranged in sequential manner.
This means that each element has a unique predecessor and successor, except for the first and last elements, respectively.

It is like one end closed box where all the operations should be done on one end.

The operations are done based on LAST IN FIRST OUT `LIFO`.

to do operations in these types of data structures, a specific order will be followed.

## Implementation of Stack

    1. list
    2. linked list
    3. deque
    4. queue.LifeQueue

1. ### Deque

   deque implementation is based on doubly linked list, where we adding operations on the right of the linked list.
   all the operation is done in O(1).

   lists are cache friendly as the elements are stored in contiguous location and the worst time complexity is linear.
   for deque, becaus individual references are at different locations, hence not cache friendly.
   all the operation of stack using this collection can be done in O(1)

2. ### Linked List

   in linked list, if we perform operation at the end(tale) of a linked list, for some operation like deleting an element or adding an element will be costly and will be done in O(N).
   for adding an element to the end of a linked list, all other elements should be traversed and can be added; Same for deletion.

3. ### list
   removing an element in list can be costly which is O(N), because we need to shift all elements to the right side of the list to the left side after removing one element.

### Application Of Stack:

- Used to handle function calls
- Reversing Items
- Balanced Parenthesis
- Stock Span Problem
- Undo/Redo or Forward/Backward
- Infix to Postfix/Prefix (a+b to ab+/+ab)
