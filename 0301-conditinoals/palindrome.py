class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False     
        div = 1
        # find the appropriate divisor
        while x >= 10*div:
            div = div * 10     
            print("div",div)   
        while x:
            right = x % 10
            left = x // div
            # compare if left and right are not the same
            if left!=right:
                return False 
            # remove the left most digit
            x = x % div
            # remove the right most digit
            x = x//10
            div = div//100
        return True
    


x = Solution()
print(x.isPalindrome(121))