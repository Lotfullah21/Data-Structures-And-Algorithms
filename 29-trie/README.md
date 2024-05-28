## Trie

It is an efficient data structure for storing and retrieving keys in a dataset.
One of its main application is spell checking and auto complete

`m` is length of the key.

| Operation                  | Trie                                          | Dictionary (Hash Table)                 |
| -------------------------- | --------------------------------------------- | --------------------------------------- |
| **Insertion**              | O(m)                                          | O(1) on average                         |
| **Search**                 | O(m)                                          | O(1) on average                         |
| **Deletion**               | O(m) (with potential cleanup)                 | O(1) on average                         |
| **Space Usage**            | Efficient for common prefixes, large overhead | Generally space-efficient               |
| **Prefix Search**          | Efficient (O(m) for prefix length)            | Inefficient, requires checking each key |
| **Sorted Order**           | Supports sorted retrieval by traversal        | Requires sorting                        |
| **Worst-case Performance** | O(m) for key length                           | O(n) due to possible hash collisions    |
