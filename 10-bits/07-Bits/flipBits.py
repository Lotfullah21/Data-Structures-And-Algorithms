class Solution:
    @staticmethod
    def maxOnes(a, n):
        count = 0
        # Check if the current indices are 1. 
        for i in range(n):
            if a[i] == 0:
                a[i] = 1
            else:
                # If 1, add to gain.
                a[i] = -1
                count += 1
        # kadan's Algorithm.
        currentSum = 0
        overallSum = float('-inf')
        for i in range(n):
            if currentSum >= 0:
                currentSum += a[i]
            else:
                currentSum = a[i]
            overallSum = max(currentSum, overallSum)
        # Check if overall sum is +ve, for instance it can be all [1, 1, 1, 1], then flipping the array would be a loss for us.
        if overallSum > 0:
            return overallSum + count
        else:
            return count

# Input
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the result
result = Solution.maxOnes(a, n)
print(result)
