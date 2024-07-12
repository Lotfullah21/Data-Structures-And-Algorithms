class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        self.dp = []
        # Create a 2-d array of size [N][W+1] to keep the previously calculated answers.
        for i in range(n+1):
            row = []
            for w in range(W+1):
                row.append(-1)
            self.dp.append(row)
        return self.knapSackHelper(W, wt, val, n)
 
    def knapSackHelper(self,W, wt, val, n):
        if n==0 or W==0:
            return 0
        if self.dp[n][W]!=-1:
            return self.dp[n][W]
        # The current weight should not exceed the current capacity of the knapsack.
        x = self.knapSackHelper(W, wt, val, n-1)
        # Only if our bag has capacity, then try to add the items.'
        y = -1
        if wt[n-1]<=W:
            y = self.knapSackHelper(W-wt[n-1], wt, val, n-1)+val[n-1]
        self.dp[n][W] = max(x,y)
        return self.dp[n][W]
    
def main():
    # Example usage
    W = 40
    wt = [10, 20, 30]
    val = [60, 100, 120]
    n = len(wt)
    solution = Solution()
    print(solution.knapSack(W, wt, val, n))  # Output should be 180 
    

if __name__ == "__main__":
    main()
        
