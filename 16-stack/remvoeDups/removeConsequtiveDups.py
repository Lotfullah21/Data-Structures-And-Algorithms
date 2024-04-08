class Solution:
    def removeDuplicates(self,string):
        stack = []
        for char in string:
            # Check if stack is empty or if not empty, the element on the top should not match to the current element, then add the current character.
            if not stack or char != stack[-1]:
                stack.append(char)
        return ''.join(stack)

# Test the function
if __name__ == "__main__":
    string = "abbbccde"
    solution = Solution()
    print(solution.removeDuplicates(string))  
