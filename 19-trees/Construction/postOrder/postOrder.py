from typing import List

class Solution:    
    def buildTree(self, In: List[int], post: List[int],n):
        for i in range(len(post)):
            self.inOrderMap[In[i]] = i

        return self.construct(post, 0, len(post) - 1, In, 0, len(In) - 1)
    
    def construct(self, post, ps, pe, In, Is, Ie):
        if ps > pe or Is > Ie:
            return None
        # The last element in post is the root of the tree
        root = TreeNode(post[pe])
        idx = self.inOrderMap[post[pe]]
        # Find the index of the root in In arr
        count = idx - Is
        # Recursively build the left and right subtrees
        root.left = self.construct(post, ps, ps + count - 1, In, Is, idx - 1)
        root.right = self.construct(post, ps + count, pe - 1, In, idx + 1, Ie)
        return root