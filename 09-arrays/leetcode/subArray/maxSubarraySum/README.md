# Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

<h2><a href="https://leetcode.com/problems/maximum-subarray/description/">leetcode</a></h2>

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

```py
def printSubArraySum(arr: list) -> list[int]:
    n = len(arr)
    subarray_sum = []
    for s in range(n):
        sum = 0
        for e in range(s, n):
            # It just adds the sum, it does not generate sub arrays.
            sum += arr[e]
            subarray_sum.append(sum)
    return subarray_sum

arr = [1, 2, 3, 4]
result = printSubArraySum(arr)
print(result)

when s = 0 and e also starts from 0 to len(array)
s = 0; e = 0
subarray = [1]
total = 0 + arr[0] = 1
subarrar_sum = [1]
s = 0; e = 1
subarray = [1, 2]
total = 1 + arr[1] = 1+2 = 3
subarrar_sum = [1,3]
s = 0; e = 2
[1,2,3]
total = 3 + arr[2] = 3 + 3 = 6
subarrar_sum = [1,3,6]
s = 0; e = 3
[1,2,3,4]
total = 6 + arr[3] = 10
subarrar_sum = [1,3,6,10]
it can continue for all other indices and generate the sum for each individual index.

```
