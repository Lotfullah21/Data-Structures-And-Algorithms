#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        # Adding the count to the trie.
        self.count = 0

class Solution:
    def klengthpref(self, arr, n, k, s):
        # Edge case: if the length of the prefix is greater than the length of the string s
        if len(s) < k:
            return 0
        # Root of the trie
        root = TrieNode()    
        # Insert all words from arr into the trie
        for word in arr:
            self.insert(root, word)
        # Search for the prefix of length k in the trie
        countOfPrefix =  self.countPrefix(root, s[:k])
        return countOfPrefix
    
    
    def insert(self, root, word):
        # Insert the word int the trie
        node = root
        for ch in word:
            i = ord(ch) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
            # For each node or character, if its new, increment it by 1.
            node.count += 1
        node.isEndOfWord = True
    
    def countPrefix(self, root, prefix):
        "Traverse the trie based on the given prefix and up to the prefix, return the count"
        node = root
        # For a prefix which will be a series of characters or strings, return number of times it occurs in the trie.
        for ch in prefix:
            i = ord(ch) - ord('a')
            if not node.children[i]:
                return 0
            node = node.children[i]
        return node.count
# Example usage:
solution = Solution()

# Example 1
arr = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
s = "abbg"
k = 3
# Match `abb` with each word in arr and see if there is a match.
print(solution.klengthpref(arr, len(arr), k, s))  # Output: 4

# Example 2
arr = ["hoosh", "hooshforhooshmand", "hooshmandlab"]
s = "hoosh"
# K is greater than len(s), it should return 0.
k = 9
print(solution.klengthpref(arr, len(arr), k, s))  # Output: 0



solution = Solution()
arr = ["apple", "app", "apricot", "banana", "bat", "bar", "barn"]
n = len(arr)
k = 3
s = "app"
print(solution.klengthpref(arr, n, k, s))  # Output: 2 (words: "apple", "app")