class Solution:
    
    def quadraticRoots(self, a, b, c):
        delta = b * b - 4 * a * c
        if delta < 0:
            return [-1]
        else:
            root1 = (-b + (delta)**0.5) / (2 * a)
            root2 = (-b - (delta)**0.5) / (2 * a)
            firstMax = max(root1, root2)
            secondMax = min(root1, root2)
        return firstMax, secondMax
