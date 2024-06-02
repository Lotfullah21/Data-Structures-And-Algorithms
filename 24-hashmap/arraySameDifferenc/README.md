## Same Differences:

You are given an array 𝑎 of 𝑛 integers. Count the number of pairs of indices (𝑖,𝑗) such that 𝑖<𝑗and 𝑎𝑗−𝑎𝑖=𝑗−𝑖.

Find pairs of indices (i, j) such that the difference between the element at each index and the index itself is the same

Input: arr = [3, 5, 1, 4, 6, 6].
Output: 1.
Explanation: there is only one pair that satisfies this condition, (j,arr[j]) = (5, 6) and (i,arr[i]) = (3, 4).

## Idea-1:

Use a brute force approach and iterate through each element in the array.
`Time Complexity`: Iterating twice, hence time complexity is `O(N^2)`.

## Idea-2:

```plaintext
arr[i]-arr[j]=i-j;
arr[j]-j = arr[i]-i;
diff = arr[i]-i;

```

keep the difference of the element and its index in the hashmap.
Compare the current difference and the count of it in the hashmap, if present, increment the answer count and increment the difference count.
If not present, simply added to the dictionary.

Here, we are storing the i-th index differences to see if in the future we need to compare with jth element and its index difference.

###

```PY
class Solution:
    def sameDifference(self, arr):
        ans = 0
        countFreq = {}
        for i in range(len(arr)):
            diff = arr[i]-i
            if diff in countFreq:
                ans+=1
                countFreq[diff]+=1
            else:
                countFreq[diff] = 1
        print(ans)
        return ans

    def diffArray(self, arr):
        diff = [0]*len(arr)




arr = [3, 5, 1, 4, 6, 6]
solution = Solution()
solution.sameDifference(arr)S
```

`Time Complexity`: Iterating once to save the difference in the hashmap `O(N)`.
`Space Complexity`: Saving the frequency of difference in the hashmap, hence, `O(N)`.
