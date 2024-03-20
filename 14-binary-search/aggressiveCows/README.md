#### Question:

You are given an array consisting of n integers which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. You are given the task of assigning stalls to k cows such that the minimum distance between any two of them is the maximum possible.
The first line of input contains two space-separated integers n and k.
The second line contains n space-separated integers denoting the position of the stalls.

<a href="https://www.geeksforgeeks.org/problems/aggressive-cows/0">GFG</a>

#### Analysis:

`Time Complexity` is `O(log(high-low)*N)`, where N is number of elements in the weights array that we need iterate over all of them to find the required days.

`Space Complexity` is `O(1)`

#### Notes:

```py
   while low<=high:
            mid = low + (high-low)//2
            cowsPlaced = self.cowsCount(mid, stalls)
            if cowsPlaced>=k:
                low = mid+1
                ans = mid
            else:
                high = mid - 1
        return ans
```

Update your answer variable to mid which is max distance, not the cowsCount.
