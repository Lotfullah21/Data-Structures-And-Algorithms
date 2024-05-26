class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def serializeHelper(root, st):
            if root is None:
                st.append("#")
                return 
            else:
                st.append(str(root.val))
                serializeHelper(root.left, st)
                serializeHelper(root.right, st)
            return ",".join(st)
        
        st = []
        serializeHelper(root, st)
        return ",".join(st)

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ...
        self.i = 0
        # Convert the current string back to a list of strings based on ',' present in between theme
        words = data.split(",")
        return self.deserializeHelper(words)
        
    def deserializeHelper(self, words):
        if words[self.i]=="#":
            self.i+=1
            return None
        else:
            # If current value is not #, make a node.
            node = TreeNode(int(words[self.i]))
            # Increment the global iterator
            self.i+=1
            # Call for the right and left child
            node.left = self.deserializeHelper(words)
            node.right = self.deserializeHelper(words)
            return node
            
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized = codec.serialize(root)
print("Serialized:", serialized)  # Output: "1,2,3,null,null,4,5"
        
    

deserialized = codec.deserialize(serialized)
print("Deserialized Root Value:", deserialized.val)  # Output: 1