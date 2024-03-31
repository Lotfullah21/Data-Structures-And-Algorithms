class Solution:
    def missingPanagram(self ,s):
        # Create a set of lowercase alphabets
        alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
        
        # Convert the input string to lowercase and create a set of its characters
        input_set = set(s.lower())
        
        # Find the difference between the alphabet set and input set
        missing_chars = alphabet_set - input_set
        
        # If all characters are present, it's a pangram
        if not missing_chars:
            return -1
        
        # Sort and join the missing characters
        result = ''.join(sorted(missing_chars))
        
        return result