## Maximum XOR of two numbers in an array

Given an array of non-negative integers of size N. Find the maximum possible XOR between two numbers present in the array.

<h3><a href="https://www.geeksforgeeks.org/problems/maximum-xor-of-two-numbers-in-an-array/1?utm_source=geeksforgeeks">GFG</a></h3>

## Idea-1:

Iterate through the array and take the xor(a^b) for every possible combination.

```py
class Solution:
    def max_xor(self, arr, n):
        #code here
        maxEle = 0
        for i in range(n):
            for j in range(i+1, n):
                if arr[i]^arr[j]>maxEle:
                    maxEle = arr[i]^arr[j]
        return maxEle
```

## Analysis:

`Time Complexity`: `O(N^2)`.
`Space Complexity`:`O(N)`.

## Idea-2:

Using Trie, traverse the tree instead of an array.

```py
class Solution:
    def checkBit(self, N,K):
        "Checks if current N's bit is 1 or 0."
        if N&(1<<K)!=0:
            return True
        return False

`(1<<i);  means move 1 by ith position to the left side.
```

`6&(1<2) = 110&100 ==True` which means the 2nd index of 6 is set.

The goal is to build the maximum XOR value bit by bit, starting from the most significant bit (MSB) down to the least significant bit (LSB).

```py
class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def max_xor(self, arr, n):
        x = max(arr)
        p = x.bit_length() -1
        # Initialize the Trie root
        self.root = TrieNode()
        # Insert each number into the Trie
        for num in arr:
            self.insert(num, p)
        ans = 0
        # Calculate the maximum XOR for each number
        for num in arr:
            ans = max(ans, self.search(num, p))
        return ans

    def insert(self, num, p):
        "insert the binary representation of num into a trie."
        node = self.root
        for i in range(p, -1, -1):
            myBit = self.checkBit(num, i)
            if myBit not in node.children:
                node.children[myBit] = TrieNode()
            # Move to the next node.
            node = node.children[myBit]

    def search(self, num, p):
        node = self.root
        b = 0
        for i in range(p, -1, -1):
            myBit = self.checkBit(num, i)
            bestBit = 1 - myBit
            if bestBit in node.children:
                # shift 1 by ith index to the left
                b = b + (1<<i)
                node = node.children[bestBit]
            else:
                # If best bit is not found, go with the flow
                node = node.children[myBit]
        return b

    def checkBit(self, n, i):
        if n&(1<<i)!=0:
            return 1
        return 0


```

## Analysis:

`Time Complexity`:
`plaintext
O(N) for finding the max in array + 
O(32*N) for searching + 
O(32*N) for insertion + 
O(32) for finding total number of bits` = `O(32*N)`
`Space Complexity`: N numbers, each is having 32 bits and each bit is occupying one node, in total `O(32*N)`
