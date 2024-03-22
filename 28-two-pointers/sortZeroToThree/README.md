### Question:

Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

`py
N = 4
arr[]= {0 1 1 2 0}
Output:
0 0 1 1 2
Explanation:
0s 1s and 2s are segregated  into ascending order
`

Lets discuss three simple ideas:

### Idea-1:

Simply use array.sort().
The time complexity would be `O(NlogN)`.

```py
class Solution:
    def sort023(self, arr: list) -> list:
        return arr.sort()

arr = [0, 0, 1, 1, 1, 2, 2]
solution = Solution()
sorted_arr = solution.sort023(arr)
print(sorted_arr)

```

### Idea-2:

Use count sort algorithm as the range of numbers are known, and it works best when there is less numbers in the array. for instance for alphabets as there are only 52 characters.

Time complexity for this idea would be `O(N + MAX(ELE))=O(N)`

```py
class Solution:
    def sort023(self, arr: list) -> list:
        # Find the max element
        maxEle = float("-inf")
        n = len(arr)
        for i in range(n):
            if arr[i]>maxEle:
                maxEle = arr[i]
        # Create an of max size
        count = [0 for _ in range(n)]
        # Find the occurrence of each element.
        for i in range(n):
            val = arr[i]
            count[val] = count[val] + 1
        # To Keep the count on the replace array.
        k=0
        for i in range(maxEle+1):
            eachEleCount = count[i]
            # Replace it in place
            for _ in range(eachEleCount):
                arr[k]=i
                k+=1

        return arr
arr = [0,1,1,1,0,1,1,2,1,2,2]
solution = Solution()
sorted_arr = solution.sort023(arr)
print(sorted_arr)
[0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2]

```

### Idea-3: Dutch National Flag

Keep in mind three regions.

- zero's regions -> (0, i-1)
- one's regions -> (i, j)
- two's regions -> (k+1, n)

What each regions have:

- (0, i-1) -> [0, 0, 0, ... ,0]
- (i, j) -> [1, 1, 1, 1, 1, 1]
- (j, k) -> Unknown
- (k+1, n) -> [2, 2, 2, 2, 2]

`0-0-0-0-0-0,i, 1-1-1-1-1, j, ?-?-?-?-?,k,2, 2, 2, 2, 2.`
How the indices looks, `ij,................k.`, keep the `ith` and `jth` index at the beginning and `k` at the end.
up to `i-1` filled with zero.
after `i` to `j` filled with ones.
from `k+1` to `n` filled with twos.
So, to keep the regions filled with the following number and find the unknown, Lets follow the following steps.

- Until the `j<=k`, continue the following steps.
- If the encountered number is `Zero`, swap that zero with the element in `i` region.
- If the encountered number is `One`, do not swap, just increment `jth` index.
- If the encountered number is `Two`, swap that 2 with `kth` index and decrement `kth index`.

```py
class Solution:
    def sort023(self, arr: list) -> list:
        self.arr = arr
        n = len(self.arr)
        i = 0
        j = 0
        k = n-1
        while j<=k:
            if self.arr[j]==0:
                self.swap(i,j)
                i+=1
                j+=1
            elif self.arr[j] == 2:
                self.swap(j, k)
                k-=1
            else:
                j+=1
        return arr

    def swap(self, i, j):
            temp = self.arr[i]
            self.arr[i] = self.arr[j]
            self.arr[j] = temp

arr = [0,1,1,1,0,1,1,2,1,2,2]
solution = Solution()
result = solution.sort023(arr)
print(result)

```

#### Analysis:

Once, we are through all the element in the array, Hence the time complexity is `O(N)` and space complexity is `O(1)`.
