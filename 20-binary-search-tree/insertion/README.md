## Insertion in Binary Search Tree

```plaintext
Input:      20
             \
              41
             / \
            40   44
X = 42
Output:    20
             \
              41
             / \
            40   44
                /
               42
```

## Iterative Approach:

<h3><a href="https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/1263682735/">leetcode-701</a></h3>

### Algorithm

- Create a new node with the given key.
- Check if root is empty:
  - Just return the new node(this is the only case the main root is changed)
- Create a temp root to traverse the tree and to avoid changing the root node every time moving to the left or right.
- Traverse the tree
  - IF current val is greater than the root.val:
    - Move to the right
    - Check if the root.right is empty, if empty make the connection and change its right ot be the new node.
    - return root or break
    - If not empty:
      - Move to right by changing the temp to be root.right
  - If current val is smaller than root.val:
    - Move to left
    - Check if root.left is empty? if empty, change its left to be the new node
    - return root or break
    - IF not empty:
      - Traverse and move to the left by changing the temp to be root.left
- return root.

```py


class Solution:
    #Function to search a node in BST.
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent = None
        temp = root
        # temp is one step a head of parent, we want to find the valid node with value None.
        while temp is not None:
            parent = temp
            if val>temp.val:
                temp = temp.right
            else:
                temp = temp.left
        newNode = TreeNode(val)
        if root is None:
            return newNode
        if val>parent.val:
            parent.right = newNode
        else:
            parent.left = newNode
        return root
```

`Time Complexity`: `O(h)`, the number of operation depends on the height of a tree, if a tree's height is more, it means we need to do more operations until we reach the lea node.
`Space Complexity`: `O(1)`, no extra space is used.

2nd iterative approach without using extra variable to keep track of the node.

```py
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if root is None:
            return newNode
        curr = root
        while True:
            if val<curr.val:
                if curr.left==None:
                    curr.left = newNode
                    break
                else:
                    curr = curr.left
            else:
                if curr.right == None:
                    curr.right = newNode
                    break
                else:
                    curr = curr.right
        return root

```

## Recursive Approach:

```py
class BST:
    #Function to search a node in BST.
   def insert(self,root, Key):
        if root == None:
            return Node(Key)
        elif root.data == Key:
            return root
        elif root.data>Key:
            root.left = self.insert(root.left, Key)
        else:
            root.right = self.insert(root.right, Key)
        return root
```

`Time Complexity`: `O(h)`, the number of operation depends on the height of a tree, if a tree's height is more, it means we need to do more operations until we reach the lea node.
`Space Complexity`: `O(h)`, because of recursive call stack.
