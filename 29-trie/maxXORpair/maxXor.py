class TrieNode:
    def __init__(self):
        self.children = {}
        
class Solution:
    def max_xor(self, arr, n):
        # Find the maximum value in the array to determine the maximum bit length needed
        x = max(arr)
        # .bit_lenght() gives the maximum number of bits required to represent a number; -1 to get the most significant bit, because of zero based indexing.
        p = x.bit_length() -1
        # Initialize the Trie root
        self.root = TrieNode()
        # Insert each number into the Trie
        for num in arr:
            self.insert(num, p)
        ans = 0
        # Calculate the maximum XOR for each number
        for num in arr:
            ans = max(ans, self.search(num, p))  
        return ans
        
    def insert(self, num, p):
        "insert the binary representation of num into a trie."
        node = self.root
        for i in range(p, -1, -1):
            myBit = self.checkBit(num, i)
            if myBit not in node.children:
                node.children[myBit] = TrieNode()
            # Move to the next node.
            node = node.children[myBit]
    
    def search(self, num, p):
        node = self.root
        b = 0
        for i in range(p, -1, -1):
            myBit = self.checkBit(num, i)
            bestBit = 1 - myBit
            if bestBit in node.children:
                # shift 1 by ith index to the left
                b = b + (1<<i)
                node = node.children[bestBit]
            else:
                # If best bit is not found, go with the flow
                node = node.children[myBit]
        return b
    
    def checkBit(self, n, i):
        if n&(1<<i)!=0:
            return 1
        return 0
    
    
    
arr = [25, 10, 2, 8, 5, 3]
n = 6
solution  = Solution()
x = solution.max_xor(arr, n)
print(x)