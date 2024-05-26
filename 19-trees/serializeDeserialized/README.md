## Serialize and Deserialize a Binary Tree

<a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/">leetcode-297</a>

### Serialization:

Serialization is the process of converting the binary tree into a string. The goal is to capture the structure and values of the tree nodes in such a way that the entire tree can be reconstructed from the string.

### Deserialization:

Deserialization is the process of converting the string representation back into the original binary tree structure. The goal here is to accurately restore the tree as it was before serialization.

## Serialization:

For serialization, we can use any kind of tree order traversal methods to traverse the tree and add the nodes into a string.

While traversing for each node.

- If the node has a value:
  - Add the str of node value to the list
- If the node has the None value:
  - Add "#" to the list
- Convert the list of strings into a whole string using `join()` method.

Here, we use preOrder traversal for serialization. One of the advantage would be that the first node in our hand would be the root node and it makes it easier while deserialization.

```py
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def serializeHelper(root, st):
            if root is None:
                st.append("#")
                return
            else:
                st.append(str(root.val))
                serializeHelper(root.left, st)
                serializeHelper(root.right, st)
            # Convert a list of strings into a whole string adding ',' between the elements of the list.
            return ",".join(st)

        st = []
        serializeHelper(root, st)
        return st
```

The only difference between main preOrder traversal and this traversal is that, in the main one, the base case was to return when you hit the None root.
Here, we have to append any kind of special character and then return.

before join method our output would look like this, the `,` appears because when adding a new element to a list, this `,` is added automatically.

`list ['1', '2', '#', '#', '3', '4', '#', '#', '5', '#', '#'],`

After using join method.

```py
Split the elements based on the `,` between them.
return ",".join(st)
```

Commas will be used a point to separate the nodes from each other.

`str "1,2,#,#,3,4,#,#,5,#,#"`

each `#` represents a node with value `None.`

## Deserialization:

Converting the string back to original tree.

## Algorithm:

- Initialize a global iterator variable
- Call the helper function inside the main function
- Inside the helper function Iterate through the string and do the following
  - If current node[i]=="#" (it acts as our base case).
    - Increment the iterator (i++)
    - return None
  - If it is a real value:
    - Create Node of the value
    - increment the iterator (i++)
    - Call for the left node
    - Call for the right node

```py
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        ...
        self.i = 0
        # Convert the current string back to a list of strings based on ',' present in between theme
        words = data.split(",")
        return self.deserializeHelper(words)

    def deserializeHelper(self, words):
        if words[self.i]=="#":
            self.i+=1
            return None
        else:
            # If current value is not #, make a node.
            node = TreeNode(int(words[self.i]))
            # Increment the global iterator
            self.i+=1
            # Call for the right and left child
            node.left = self.deserializeHelper(words)
            node.right = self.deserializeHelper(words)
            return node
```

## Analysis:

`Time Complexity`: For each of the function, the whole tree or whole string is traversed, so `O(N)+O(N) = O(N)`.
`Space Complexity`: The only space in use recursive call stack.
