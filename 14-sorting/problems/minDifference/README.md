### Question:

Given an array of n length integers, find the minimum difference between the elements in the given array.

Input: [1, 5, 0, 9, 10]
Output: (10-9) = 1

### Idea-1:

```py
def minDifference(arr: list) -> int:
    "Returns the min difference between two arrays."
    n = len(arr)
    ans = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            ans = min(ans, abs(arr[i]-arr[j]))
    return ans


arr = [1,92,32 ,4321, 2132, 42, 433,45]
result = minDifference(arr)
print(result)

```

### Analysis

`Time complexity`: `O(N^2)`, For each element, we have compare to other n-1 elements.
`Space Complexity`: `O(1)`, No extra space is used.

### Idea-2:

- Sort the array
- Return the minimum value between two adjacent element.

```py
def minDifference(arr: list) -> int:
    "Returns the min difference between two arrays."
    n = len(arr)
    ans = float("inf")
    arr.sort()
    for i in range(n-1):
        ans = min(ans, abs(arr[i]-arr[i+1]))
    return ans

arr = [1,92,32 ,4321, 2132, 42, 433,45]
result = minDifference(arr)
print(result)

```

### Analysis

`Time complexity`: `O(NlogN)`, because of sorting the array..
`Space Complexity`: `O(1)`, No extra space is used.
