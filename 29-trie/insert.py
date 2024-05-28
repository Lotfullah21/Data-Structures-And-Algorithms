#User function Template for python3


class Trieroot: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if root represent the end of the word 
        self.isEndOfWord = False


class Solution:
    #Function to insert string into TRIE.
    def insert(self, root, key):
        for x in key:
            i = ord(x)-ord('a')
            if root.children[i] is None:
                root.children[i] = Trieroot()
            root = root.children[i]
        root.isEndOfWord = True
                
    
    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        for x in key:
            i = ord(x)-ord('a')
            if root.children[i] is None:
                return False
            root = root.children[i]
        return root.isEndOfWord