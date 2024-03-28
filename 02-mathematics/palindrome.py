class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False     
        div = 1
        # Find the appropriate divisor, and enter this loop again and again until you find the divisor that is at least not greater than x.
        # take that as divisor go to next loop.
        while x >= 10*div:
            div = div * 10     
            print("div",div)   
        # until x is not 0.
        while x:
            # right most digit 
            right = x % 10
            # left most digit, 121//100 = 1
            left = x // div
            # compare if left and right are not the same
            if left!=right:
                return False 
            
            # remove the left most digit
            x = x % div
            # remove the right most digit
            x = x//10
            # since we are removing two digit from left and right, divide 100.
            div = div//100
        return True
    


x = Solution()
print(x.isPalindrome(121))
print(1221%10)
print(121//10)