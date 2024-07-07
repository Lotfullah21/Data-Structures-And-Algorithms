## Hashing

Hashing is mainly used to implement dictionaries ans sets.
In Hashing, we are always having unique values, duplicates are not allowed. If an element is already existed, adding a the same key will overwrite the previous key.

In hashing, we can implement `search, insert and delete` operations in constant time `O(1)`.

For instance if insertion into a list is done in unsorted order, the `search` operation will take linear time, if insertion is done in sorted order, then the `search` operation takes `logN` operations, but insertion takes `O(N)` operations.

Hashing is not best for the following operations:

- Finding closest value
- Keeping the data in sorted order
- Prefix search

| Data Structure     | Search   | Insert | Delete | Comments                                              |
| ------------------ | -------- | ------ | ------ | ----------------------------------------------------- |
| Unsorted List      | O(n)     | O(1)   | O(n)   | Fast insertion, slow search and deletion              |
| Sorted List        | O(log n) | O(n)   | O(n)   | Binary search for fast lookup, but slow insertion     |
| Singly Linked List | O(n)     | O(1)   | O(n)   | Fast insertion, slow search and deletion              |
| Doubly Linked List | O(n)     | O(1)   | O(n)   | Fast insertion, slow search and deletion              |
| Hash Table         | O(1)     | O(1)   | O(1)   | Average case constant time for search, insert, delete |

## Application:

- Dictionary implementation
- Database indexing to find the records quickly
- Using keys and getting the values from the database
- Implementing caching associated to an url
- Cryptography
- To check if a symbol is valid or not in compilers/interpreters
