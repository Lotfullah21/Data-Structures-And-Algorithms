class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):  
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            
    def findMaxXOR(self, num):
        node = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if 1 - bit in node.children:
                xor |= (1 << i) 
                node = node.children[1 - bit]
            else:
                node = node.children[bit]
        return xor

class Solution:
    def maxSubarrayXOR(self, N, arr):
        trie = Trie()
        maxXOR = float('-inf')
        preXOR = 0
        trie.insert(0)  
        for num in arr:
            preXOR ^= num
            maxXOR = max(maxXOR, trie.findMaxXOR(preXOR))
            trie.insert(preXOR)
        return maxXOR
