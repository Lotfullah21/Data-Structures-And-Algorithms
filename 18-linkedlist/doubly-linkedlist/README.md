## Doubly Linked List:

in doubly linked list, every node has a reference to its previous and its next node.

#### Advantages:

- Can be traversed in both directions, practical use case would browsing history where the user can go previous tabs.
- A node can be deleted in O(1) time,given the reference. easily change the pointers where in singly linked list, the list up to the point should be traversed.
- Insert/Delete a node from both end in O(1) time,for singly linked list, it is not possible to delete the tail in O(1).

#### Disadvantage:

- Extra space to keep the prev pointer
- Adding complexity to the code.
