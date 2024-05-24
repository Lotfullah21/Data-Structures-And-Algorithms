def LCA(root, n1, n2):
    # If root is not empty, traverse through the tree starting from the root node.
    while root:
        # If both n1 and n2 are greater than root, LCA lies in the right subtree
        if root.data>n1 and root.data>n2:
            root = root.left
        elif root.data<n1 and root.data<n2:
            root = root.right
        else:
            return root
    return None



class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Helper function to insert a new node with the given key
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
    # IF current key is smaller, make it left child
    if key < node.data:
        node.left = insert(node.left, key)
    # IF current key is greater, make it right child
    else:
        node.right = insert(node.right, key)
    return node

# Example 
root = None
keys = [6, 5, 7, 4, 12, 14]
for key in keys:
    root1 = insert(root1, key)

n1, n2 = 12, 6
lca1 = LCA(root1, n1, n2)
print(f"The LCA of {n1} and {n2} is {lca1.data}" if lca1 else "LCA not found")
