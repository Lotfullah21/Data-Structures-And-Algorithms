from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def zigZagTraversal(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    current_level.append(node.data)
                else:
                    current_level.insert(0, node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            left_to_right = not left_to_right
            result.extend(current_level)

        return result
