#### Google

### Question:

given an array of length n, all sorted except the last element, sort the array in `O(n)` time.

#### Idea-1:

use `array.sort()`, but the time complexity is `O(NlogN)`.

### Idea-2:

the last element is not sorted.
Start comparing the last element with the previous element in the array.
If prev is greater than the current, swap them.
Break once the previous element is not greater than the current element.

```py
class Solution:
    def sortFirstNth(self, arr: list) -> list:
        n = len(arr)
        for j in range(n-2, -1, -1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        return arr
solution = Solution()
arr = [1, 2, 3, 4 ,5, 0]
sortedArray = solution.sortFirstNth(arr)
print(sortedArray) ## [0, 1, 2, 3, 4, 5]


```

ime complexity is `O(N)` and space complexity `O(1)`.
