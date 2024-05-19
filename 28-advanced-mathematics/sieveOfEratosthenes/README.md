### Question

given a number, print prime numbers up to n, including n.

#### Idea-1: Brute Force

```py
class Solution:
    def isPrime(self, n):
        "Returns True if a given n is a prime number."
        count = 0
        for i in range(1, int(n**0.5)+1):
        # for i in range(1, n+1):
            if n%i==0:
                count+=1
        if count==2:
            return True
        else:
            return False

    def printPrime(self,n):
        "Returns prime numbers up to n, including n."
        primeNumbers = []
        for i in range(2,n+1):
            #
            if self.isPrime(i):
                primeNumbers.append(i)
        return primeNumbers

```

## sieveOfEratosthenes Algorithm

To find Prime numbers from a given range, it can be achieved by crossing out the multiples of numbers starting from `2` and continue up to `sqrt(N)`;

#### Steps:

- Create boolean array of size `N`
- Initially fill it with `True` boolean value.
- Fill 0th and 1st index with `False` boolean value.
- Start from `i` to `sqrt(n)`
  - Check if that index is already have the value of `True`.
  - For each `i`, start from twice of `i` == `(2*i)`.
  - Increment by `i` and make the array `False` for those `i`s.
- return the indices that are having `True` value after the above steps.

### Notes to avoid bugs:

- create an array of n+1, because in line 11, it will give error of before assignment due to mismatch between the size and last index.
- for adding primes to the list, line 15, go through n+1, otherwise, you will miss the last element which might be a prime number.

#### Analysis:

`Time Complexity` is `O(loglogN)~= O(logN)` as we are taking N/2 steps in each function call to reach to 0.
`Space Complexity` is `O(N)` is the boolean array we used for storing the bool values.

<a href="./https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/0"><>
<a href="">GFG</a>
