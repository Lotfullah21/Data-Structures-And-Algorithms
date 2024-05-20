# Binary Search Tree

A binary tree is a Binary Search Tree if it has the following properties:

- The left subtree of the root node contains only nodes strictly smaller than the root node's data.
- The right subtree of the root node contains only nodes strictly greater than the root node's data.
- The right and left subtree, each must be a binary search tree.

In an0ther words, a binary tree is a binary search tree if for all the nodes, the nodes on the left side are smaller than the root node and nodes on the right side are larger than the root node. This property in addition to the the root node, should be valid for each individual sub tree.

It is a linked data structure and when we need more memory, there is no need of resizing, just link the new element to the tree.

It cannot contain duplicate nodes, each node value is distinct.

### Binary Tree:

A tree is a binary tree if it has at most two children for a root.

```plaintext
       1
      / \
     2   3
    / \   \
   4   5   6

```

A tree can be a binary search tree or just a binary tree.

### Balanced Tree:

A balance tree is a tree where the height difference between the left and right subtree is minimized.

Balanced Tree

```plaintext
  20
 /  \
10  30

```

UnBalanced Tree:

```plaintext
  20
 /  \
10  30
      \
      40
        \
        60
          \
           70
            \
             80
              \
              90

```

The main advantage of balanced BST is that all the operations like searching, insertion, deletion and finding closest value can be done in `O(logN)` time, because of its optimal structure.

But, for unbalanced, these operations becomes costly which is proportional to the heigh of a tree `O(h)`, which in worst case we might be having `N` nodes, so it becomes `O(N)` .

There are different kinds of binary search tree, in the given table a comparison is done between them.

```table

| **Property/Operation** | **B-Tree**               | **AVL Tree**          | **Red-Black Tree**   | **Splay Tree**         |
|------------------------|--------------------------|-----------------------|----------------------|------------------------|
| **Search**             | O(log n)                 | O(log n)              | O(log n)             | O(log n) (amortized)   |
| **Insertion**          | O(log n)                 | O(log n)              | O(log n)             | O(log n) (amortized)   |
| **Deletion**           | O(log n)                 | O(log n)              | O(log n)             | O(log n) (amortized)   |
| **Height Balance**     | Balanced (multi-way)     | Strictly balanced     | Loosely balanced     | Self-adjusting         |
| **Rotation Overhead**  | None (node splitting)    | High (single/double)  | Moderate (single)    | None during access     |
| **Tree Structure**     | Multi-way                | Binary                | Binary               | Binary                 |
| **Use Case**           | Databases, file systems  | Read-heavy workloads  | General use          | Frequently accessed    |
| **Memory Usage**       | Moderate to high         | Higher due to balance | Lower than AVL       | Low to moderate        |
| **Implementation**     | Complex                  | Complex               | Moderate             | Simple                 |
| **Additional Features**| M nodes per node (M-ary) | Strict balance factor | Red/black coloring   | Splaying (self-adjust) |


```
