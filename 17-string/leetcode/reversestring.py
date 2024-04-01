class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0 
        end = len(s) - 1
        while (start<end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start+=1
            end-=1

        