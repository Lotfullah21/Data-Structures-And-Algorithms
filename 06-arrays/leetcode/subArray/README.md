For getting total values of sub array, we are going to study two ideas

### Idea-1

go through all indices and print their prefixes.
`Time Complexity` for this idea would be `O(N^2)` and `Space Complexity` is `O(N)` because of creating prefix sum array and using it.

```py
def printSubArraySum(arr: list) -> list:
    n = len(arr)
    pf = [0]*n
    pf[0] = arr[0]
    # Create the prefix array sum.
    for i in range(1,n):
        pf[i] = pf[i-1]+arr[i]
    print(pf)
    # Keep a reference to total variable
    total = 0
    for s in range(n):

        for e in range(s, n):
            if s==0:
                total = pf[e] + total
            else:
                total  = pf[e]-pf[s-1] + total
    return total
```

### Idea-2:

get the occurrence of each element and count them, the number of times each element appears in subArray, that much it contributes to our total sum.

`Time Complexity` for this idea would be `O(N)` and `Space Complexity` is `O(1)`.

```py
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

```
