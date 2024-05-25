## Delete Node in a BST

Given a BST with a root node reference and a key, delete the node with the given key. By deleting the node with the given key, the BST properties should be maintained.

<h3><a href="https://leetcode.com/problems/delete-node-in-a-bst/">leetcode-450</a></h3>

## Solution:

Two steps to be followed:
First, we have to find the node with the given key.
Second: Deletion of the node once found.

### Searching:

For searching,
Compare the current key with the root node.

1. If roo.val>key:
   1. Go to left
   2. Make the root to be the left node(root = root.left)
2. If roo.val<key:
   1. Go to right
   2. Make the root to be the right node(root = root.right)
3. If root.val == key:
   1. Do the Deletion operation.

### Deletion:

We are having four scenarios a head.

1. #### Leaf Node :

If the node to be deleted has no left and right child.

In this scenario, the node is a leaf node. just return None from that node and the node will be deleted.

`Key = 2`;The node to be deleted is a node with value=2.

```plaintext
    5
   / \
  3   7
 / \
2   4

```

1. Start with the root node, 5>3;
   1. Move to left
   2. root = root.left => root = 3;
2. Compare 3 with 2; 3>2:
   1. Move to left
   2. root = root.left => root = 2;
3. 2==2; Root to be deleted found.
   1. return None or make the 3.left = None.

Output:

```plaintext

    5
   / \
  3   7
   \
    4
```

2. ### Left Child

If the node to be deleted only has a left child.

return its left child to be the left child of its parent.

`Key = 5`; The node to be deleted is a node with value=5.

```plaintext
       6
      / \
     5   7
    /
   2
  / \
 1   3
```

It can be observed that it has only left child.
Traverse through the tree, find the root with given key, deleted the node by breaking the chain and returning its left child.

1. Start with the root node, 6>5;
   1. Move to left
   2. root = root.left => root = 5;
2. Compare 5 with 5; 5==5:

   1. Root has been found, return its left child to its parent
   2. return root.left => 5.left => node with value 2 => node(2)

3. ### Right child

If the node to be deleted has only right child.

`Key = 2`; The node to be deleted is a node with value=2.

```plaintext
    6
   / \
  5   7
 /
2
 \
  3
   \
    1

```

1. Start with the root node, 6>2;
   1. Move to left
   2. root = root.left => root = 5;
2. Compare key=2 with root.val=5; 5>2:
   1. Move to left
   2. root = root.left => root = 2;
3. Compare key=2 with root.val=2; 2==2:

   1. Root has been found, return its right child to its parent(node(5));
   2. Make left of parent to be right of the node to be deleted;
   3. return node(5).left = root.right => node(5).left = node(2).right;

4. ### Right Child and Left Child:

If the node to be deleted has both the right and left child, if we delete immediately, the bst property will be lost.
First, we have to find a proper value to replace it.
Second, delete it.

To find a proper a value to replace current root.
Find the maximum among its left children and replace with the node's value we want to delete.
By swapping the maximum from left children, we are maintaining the BST property. All elements on the left side will be smaller than the root node.

#### 4.1 Finding max node on the left side.

- The maximum on the left side is the right most children.
- Traverse the tree and find the max.
- Keep it in a variable
- Change the value of the node to be deleted with the maximum value.
- Then Traverse the tree to delete the node with the maximum value.

`Key = 3`; The node to be deleted is a node with value=3.

```plaintext
    5
   / \
  3   7
 / \
2   4

```

The node with the given key have two children,

1. left child = node(3)
2. right child = node(4)

We cannot delete the node directly, first we have to find the maximum among left children of node(3), then make that the current root.
It can be observed that the right most element of child 2 is 2;

- max = node(2)
- node(3).val = 2
- delete node(2)
- node(2) is a leaf node, so return `None.`

Output:

```py
    5
   / \
  2   7
   \
    4

```

### Analysis;

Three Functions are called
Initial Search: O(h)
Finding Max in Left Subtree: O(h)
Recursive Deletion: O(h)

#### Overall Time Complexity

Combining these steps, the overall time complexity for the deleteNode function is: `O(h)+O(h)+O(h)=O(h)`
`O(h)` can be `O(logN)` in the best case when the tree is balanced and `O(N)` when tree is not balanced(skewed in one direction).

#### Overall Space Complexity:

Three function stacks call, but still `O(h)` ignoring constant terms.
