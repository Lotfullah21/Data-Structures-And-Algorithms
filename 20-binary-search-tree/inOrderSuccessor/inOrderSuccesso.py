class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.right = None
        self.left = None
    
    
    
    def inOrderSuccessor(self, root, k):
        ans = None
        # Find the target node with value k.
        while True:
            # If root's value is greater than k, save that and move to the left, because that might our potential answer.
            if root.val>k:
                ans = root
                root = root.left
            # If root's value is smaller than k, move to the right side, because we are looking for greater elements.
            elif root.val<k:
                root = root.right
            # root == k
            else:
                break
        # If no node on right side of target node, the potential answer we saved while traversing to the left side is our answer.
        if root.right==None:
            return ans
        # If right side of target root with value k is not None, answer is on the left most side of that right node.
        rightRoot = root.right
        while rightRoot.left!=None:
            rightRoot = rightRoot.left
        return rightRoot
            
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Build the example BST.
root = TreeNode(20)
insert(root, 10)
insert(root, 30)
insert(root, 5)
insert(root, 15)
insert(root, 25)
insert(root, 35)

# Create a TreeNode instance and find the in-order successor.
node = TreeNode()
successor = node.inOrderSuccessor(root, 20)
if successor:
    print(f"The in-order successor of 20 is {successor.val}")
else:
    print("The in-order successor of 20 does not exist.")