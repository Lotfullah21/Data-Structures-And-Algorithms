#### Question:

Given an integer N, from 1 to N, count how many numbers are there that have exactly three divisors.

#### Idea-1:

count number of divisors for each integer.

inside another function for all numbers less than n, find their divisors, if ==3, return True.

```py
import math

class Solution:
    def countNumbersWith3Divisors(self, N: int) -> int:
        """
        Returns the count of numbers less than or equal to N
        that have exactly 3 divisors.
        """
        count = 0
        for i in range(2, N + 1):
            if self.countDivisors(i) == 3:
                count += 1
        return count

    def countDivisors(self, n: int) -> int:
        """
        Returns the number of divisors of integer n
        """
        divisors = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                # If divisors are same, increment once.
                if n // i == i:
                    divisors += 1
                # Otherwise, increment twice.
                else:
                    divisors += 2
        return divisors
```

#### Analysis:

`Time Complexity` is `O(N*sqrt(N))` as we are checking from 1 to sqrt(n) to find the divisors and 1 to N to find divisors of numbers less than n.
`Space Complexity` is `O(1)` no extra space is used.

Prime numbers have exactly 2 divisors: 1 and the number itself. This is a fundamental property of prime numbers.
However, when we square a prime number, the resulting number has exactly 3 divisors: 1, the prime number itself, and the square of the prime number.

For example:
The prime number 2 has 2 divisors: 1 and 2.
The square of 2, which is 4, has 3 divisors: 1, 2, and 4.
This property holds true for all prime numbers. When we square a prime number, we get a number with exactly 3 divisors. This is why in the code, we count the number of prime numbers i such that i\*i is less than or equal to N, to find the count of numbers less than or equal to N that have exactly 3 divisors.

In essence, the code is leveraging this property to count the numbers with exactly 3 divisors efficiently by counting the prime numbers within the given range.
