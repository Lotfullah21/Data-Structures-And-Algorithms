def printSubArraySum(arr: list) -> list:
    n = len(arr)
    ans = 0
    for i in range(n):
        occurrence = (i+1)*(n-i)
        ans = ans + occurrence * arr[i]
    return ans
                  
arr = [5,3,-1,8]
result = printSubArraySum(arr)
print(result)

