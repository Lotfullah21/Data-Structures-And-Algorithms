#User function Template for python3

class Solution:
    def sumUnderModulo(self,a,b):
  
        MOD = 10**9 + 7
        
        # Calculate the sum
        sum_ab = a + b
        
        # Take the modulo
        result = sum_ab % MOD
        
        return result
    
# Test Case 1
a1 = 9223372036854775807
b1 = 9223372036854775807
solution = Solution()
result1 =solution.sumUnderModulo(a1, b1)
print("Output for Test Case 1:", result1)

# Test Case 2
a2 = 1000000007
b2 = 1000000007
result2 = solution.sumUnderModulo(a2, b2)
print("Output for Test Case 2:", result2)
