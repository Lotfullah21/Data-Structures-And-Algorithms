def findNthFibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # Initialize dp array
    dp = [0] * (N + 1)
    dp[0] = 0
    dp[1] = 1
    
    # Fill the dp array using the bottom-up approach
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[N]

# Example usage:
N1 = 5
print(findNthFibonacci(N1))  # Output: 5

N2 = 7
print(findNthFibonacci(N2))  # Output: 13
