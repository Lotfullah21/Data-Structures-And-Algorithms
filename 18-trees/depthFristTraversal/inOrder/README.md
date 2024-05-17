## InOrder Traversal

Given a Binary Tree, return the keys using inOrder traversal.

Example 1:

```plaintext

Input:
       1
     /  \
    3    2
Output: 3 1 2

Input:
        10
     /      \
    20       30
  /    \    /
 40    60  50

Output: 40 20 60 10 50 30
```

<h3><a href="https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/tree-basic-python/problem/inorder-traversal">GFG</a></h3>

## Note:

Remember to do not add the `result` list inside the recursive function, because every time it resets and removes the previous values if they were added.

Use one helper function to do the recursive calls, and one main function to have the result list, to call the recursive function, and to return the result.

```py
class Solution:
    def inorderTraversal(self, root) -> List:
        result = []
        self.inOrderHelper(root,result)
        return result
    def inOrderHelper(self, root, result):
        if root!=None:
            self.inOrderHelper(root.left, result)
            result.append(root.data)
            self.inOrderHelper(root.right, result)

```

Or this one.

```py

class Solution:
    def InOrder(self,root):
        # code here
        result = []
        def helper(root, result):
            if root==None:
                return
            helper(root.left,result)
            result.append(root.data)
            helper(root.right,result)

        helper(root, result)
        return result


```
