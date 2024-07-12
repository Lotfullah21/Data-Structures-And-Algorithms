class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,N,W, val, wt):
        self.dp = []
        # Create a 2d array.
        for _ in range(N+1):
            row = []
            for w in range(W+1):
                row.append(-1)
            self.dp.append(row)
        return self.knapSackHelper(N,W,val,wt)
 
    def knapSackHelper(self,N,W, val, wt):
        # Base case, no item left or no capacity left.
        if N==0 or W==0:
            return 0
        if self.dp[N][W]!=-1:
            return self.dp[N][W]
        included = self.knapSackHelper(N-1,W, val, wt)
        excluded = -1
        # If and only if the weight of current weights indices are smaller than the current capacity, then reduce and include.
        if wt[N-1]<=W:
            excluded = self.knapSackHelper(N, W-wt[N-1], val, wt)+val[N-1]
        self.dp[N][W] = max(included, excluded)
        return self.dp[N][W]

def main():
    # Usage example
    N = 3  # Number of items
    W = 50  # Capacity of knapsack
    val = [60, 100, 120]  # Values of items
    wt = [10, 20, 30]  # Weights of items
    solution = Solution()
    max_value = solution.knapSack(N, W, val, wt)
    print(f"The maximum value that can be put in the knapsack of capacity {W} is {max_value}")

if __name__ =="__main__":
    main()