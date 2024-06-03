## Subarrays with equal 1s and 0s

Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

<h2><a href="https://www.geeksforgeeks.org/problems/count-subarrays-with-equal-number-of-1s-and-0s-1587115620/1?utm_source=gfg">GFG</a></h2>

## Idea-1:

Replace zeros in the array with -1.
Calculate prefix sum.
Then using summation in prefix sum array

#### Algorithm:

```bash

sum(start, end) = k
pf[end]-pf[start-1] = k
pf[end] - k = pf[start-1]
Find the value for right hand side.
Create a dictionary where the keys are the result of pf[end] - k and values are the number of its occurrence.
If the calculated difference existed in the dictionary (its count is >0), it means we are having one starting value that sums up to K.
    - Increment the answer and also increment frequency of that value to freq hashmap.
If not present.
    - Increment the frequency and move to the index index.

Edge Case:

When pf[end] - k ==0, it means, the k itself present in the array.
Two ways to handle:
Write one conditional statement whenever prefix[end]==0:
    - Increment the answer by 1.
Or, add a predefined key-val in freq hashmap {0:1}.
    - Because the way the answer variable is incremented is by finding the value in the freq map if it is present, we are incrementing the answer.
    - Now, whenever pf[end] - k ==0, the count of 0 is already in dictionary, simply increment it.

```

```py

#User function Template for python3
class Solution:
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        freq = {0:1}
        ans = 0
        k=0
        # Replace the index with the element equal to zero to -1.
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=-1
        # Calculate prefix for the new array.
        pf = self.prefixSum(arr)
        for end in range(len(arr)):
            diff = pf[end]-k
            if diff in freq:
                ans+=freq[diff]
            if pf[end] not in freq:
                freq[pf[end]]=1
            else:
                freq[pf[end]] += 1
        return ans

    # Function to get prefix sum of an array.
    def prefixSum(self,arr):
        pf = [0]*len(arr)
        for i in range(len(arr)):
            pf[i] = pf[i-1]+arr[i]
        return pf

```

### Analysis:

`Time and Space complexity is O(N)`, refer to <a href="../subArraySumEquallsK/README.md">description</a>.

## Idea-2: Prefix Count

Count the prefix count of an array if the element we are checking is zero and one.
Calculate if the difference is the same which means from range a to range b, same number of zeros and ones added to each respectively, then increment the answer.

The efficiency is same as the first approach, but the latter one is more generic and can be applied when the numbers are not only ones and zeros.
