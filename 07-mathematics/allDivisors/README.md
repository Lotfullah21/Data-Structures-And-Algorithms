### Question:

Given an integer, print all integers that are divisors of given integer.
For example:
Input: 8
Output: 2, 4, 8
Explanation: 8%1==0, 8%2==0, 8%4==0 and 8%8==0

#### Idea-1:

Go through all numbers less than given integer ana check if those numbers can divide given integer perfectly.

```py
def divisors(n: int) -> list[int]:
    "returns divisors of integer n"
    divisors = []
    for i in range(1, n+1):
        if n%i==0:
            divisors.append(i)
    return divisors
```

#### Analysis:

`Time Complexity` is `O(N)` as we are checking from 1 to N.
`Space Complexity` is `O(1)` no extra space is used.

#### Idea-2:

Using pair divisors.

##### Divisors of 48:

1. 1
2. 2
3. 3
4. 4
5. 6
6. 8
7. 12
8. 16
9. 24
10. 48

##### Pairs of Divisors:

1. (1, 48)
2. (2, 24)
3. (3, 16)
4. (4, 12)
5. (6, 8)

Each of these pairs multiplies together to give 48:

1.  1 \* 48 = 48
2.  2 \* 24 = 48
3.  3 \* 16 = 48
4.  4 \* 12 = 48
5.  6 \* 8 = 48

to generalize:

One of the divisor in every pair is less than or equal to `sqrt(n)`; for a pair `X*Y=N`, lets say `X<Y`, then

```math
X * Y <=N
X * X <= N/(sqrt())
sqrt(X*X) <= sqrt(N)
X <= sqrt(N)


```

From above pairs, it can observed that there is no need of going up to `n` iterations to find `divisors` of `n`.

go up to `square root of n`, if a number less than `sqrt(n)` is a divisor, to get the other number, just divide the `n//current divisor`

```py
import math
def divisors(n: int) -> list[int]:
    "returns divisors of integer n"
    divisors = []
    i = 1
    while int(i<=(n**0.5)):
        if n%i==0:
            divisors.append(i)
            # If the number has perfect square, it will be appended twice; One time in each if condition.
            if n//i!=i:
                divisors.append(n//i)
        i+=1
    return divisors
```

#### Idea-3:

Lets implement the idea in such a way that the divisors are appended in sorted order.

#### Analysis:

```py

import math
def divisors(n: int) -> list[int]:
    "returns divisors of integer n"
    divisors = []
    i = 1
    # Divisors from 1 to sqrt(n), sqrt(n) excluded.
    while i<(math.sqrt(n)):
        if n%i==0:
            divisors.append(i)
        i+=1
    # Now variable i increased from 1 to some larger number.
    # from  sqrt(n), sqrt(n) Included.
    while i>=1:
        # The perfect square numbers will be handled here.
        if n%i==0:
            divisors.append(n//i)
        i = i - 1
    return divisors
```

For smaller divisor than `sqrt(n)`, go up to `sqrt(n)`, and now the `i` has reached less than or equal to `sqrt(n)`.
From this point, write another loop same as idea-1.
