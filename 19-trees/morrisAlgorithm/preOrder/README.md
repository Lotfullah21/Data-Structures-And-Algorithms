## Binary Tree Preorder Traversal

<h3><a href="https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1269307006/">leetcode-144</a></h3>

All the procedures same as inorder traversal but wiht one difference, before moving to the left side, process the current root.

<h3><a href="../inOrder/">inorder</a></h3>

```py

                # Make the connect between the right most node of left child and the current root.
                if currp1.right is None:
                    currp1.right = curr
                    # Before moving to the left side, process the current root.
                    res.append(curr.val)
                    # Move to left of current node.
                    curr = curr.left
                else:
                    # Restore the order
                    currp1.right = None
                    # Move to the right of current node.
                    curr = curr.right

```
