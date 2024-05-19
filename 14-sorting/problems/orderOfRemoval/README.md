#### Question:

Given an array of elements, remove the elements in such a way that the total cost of removal is minimum.
Cost of removal = sum of all elements present including the element to be removed.

Input: [1, 2, 3, 4]
Output: 20
Explanation: Remove the max elements first, because every one element is removed, that element no longer contributes anything.

[1, 2, 3, 4]
remove 4; cost = 1+2+3+4 = 10
remove 3: cost = 1+2+3 = 6
remove 2: cost = 1+2 = 3
remove 1: cost = 1 = 1
total cost = 20

It can be observed that the element at the 0th index contributes and repeated maximum number of times, as the index increase the contribution of that element is reduces.

#### Idea:

Sort the array and remove the largest element at each iteration.
How to remove the largest element: Start from last index.

How to implement in code.
It can be observed that each element is added to the total cost by (len(array)-index)\*element.

```py
def minCost(array: list) -> int:
    "Remove the elements in such an order that the total cost is minimum at the end."
    answer = 0
    n = len(array)
    array.sort()
    for i in range(n-1, -1, -1):
        contribution = n - i
        answer = answer + array[i]*contribution
    return answer

array = [5,1, 2, 3, 4]
result = minCost(array)
Output: 35
```

#### Analysis:

`Time Complexity`: sorting array takes `O(NlogN)` and traversing through whole array takes `O(N)`.
total = `O(NlogN)`+`O(N)` = `O(NlogN)`
`Space complexity`: No extra space is used.
