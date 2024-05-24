# Node mold
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.right = None
        self.left = None
        
        
class Solution:
    def populate(self, root):
        if root is None:
            return 
        answer = root
        while (root.left!=None):
            temp = root
            while temp is not None:
                if temp.left:
                    temp.left.next = temp.right
                if temp.right and temp.next:
                    temp.right.next = temp.next.left
                # After setting the left and right of a node, go to the next node of current root.
                temp = temp.next
            # The moment the temp becomes None, go to next level.
            root = root.left
        return answer
        
head = TreeNode(8)
head.left = TreeNode(5)
head.right = TreeNode(14)
head.left.left = TreeNode(4)
head.left.right = TreeNode(6)
head.right.left = TreeNode(13)
head.right.right = TreeNode(16)

solution = Solution()
solution.populate(head)



def printNext(root):
    while root:
        current = root
        while current is not None:
            if current.next:
                nextValue = current.next.val
            else:
                nextValue = "End Of level"
            print(f"Node {current.val} -> Next {nextValue}")
            current = current.next
        root = root.left
        
        
printNext(head)