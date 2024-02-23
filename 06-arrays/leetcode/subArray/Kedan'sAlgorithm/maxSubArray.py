def maxSubArray(arr):
    # Kee a reference for sum
    sum = 0
    # Initial answer 
    ans = float("-inf")
    n = len(arr)
    for i in range(n):
        if sum>=0:
            sum = sum + arr[i]
        else:
            sum = arr[i]
        ans  = max(ans, sum)
    return ans

        
        