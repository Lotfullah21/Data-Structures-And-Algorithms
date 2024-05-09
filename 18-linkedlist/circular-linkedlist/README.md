## Circular Linked List:

A list where the next of last node is head.

### Advantages:

- Linked list can be traversed from any node.
- By having only one variable, insertion/deletion can be done at the end and beginning of the linked list.
  - helpful for Queue implementation(insertion from front and deletion from end)
  - Adding or deleting a node is just adding a node between the tail and head.
    - Insertion in head: Make the next of tail as the new node.
    - Deletion in tail: Update prev of tail to point to the head.

### Disadvantage:

Implementation of operations like traversal, insertion in the middle becomes complex.
