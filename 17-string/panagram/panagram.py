def isPanagram(s):
    s.lower()
    # Create a set to add unique characters
    uniqueChars = set()
    # Check for all characters
    for i in range(len(s)):
        # Check if char is alphabetic.
        if s[i].isalpha():
            uniqueChars.add(s[i])
            
    if len(uniqueChars)==26:
        return True
    else:
        return False
    
