class Trieroot:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
#Function to insert string into TRIE.     
def insert(root,key):
    #code here
    node = root
    for ch in key:
        i = ord(ch)-ord('a')
        # If children of current root is None with this index, add a new node and save its address at this index.
        if node.children[i] is None:
            node.children[i] = Trieroot()
        # Make the newly created node the new root.
        node = node.children[i]
    # After Adding all characters, make the last node to have value True for its child node to indicate it is the last word.
    node.isEndOfWord = True
    

#Function to use TRIE data structure and search the given string.
def search(root, key):
    #code here
    node = root
    for ch in key:
        i = ord(ch)-ord('a')
        # If no child at current index, it shows absence of current character, so return False.
        if node.children[i] is None:
            return False
        # Go to next node
        node = node.children[i]
    # Return True only if complete word is present.
    if node.isEndOfWord==True:
        return True
    else:
        return False
    # Shorter
    # return node.isEndOfWord
    
# Creating a new Trie root
root = Trieroot()

# Inserting words into the Trie
insert(root, "hello")
insert(root, "world")
insert(root, "hi")
insert(root, "her")
insert(root, "hero")

# Searching for words in the Trie
print(search(root, "hello"))  # Output: True
print(search(root, "world"))  # Output: True
print(search(root, "hero"))   # Output: True
print(search(root, "her"))    # Output: True
print(search(root, "he"))     # Output: False
print(search(root, "help"))   # Output: False